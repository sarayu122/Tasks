import uuid
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename

from config import ALLOWED_EXTENSIONS, SECRET_KEY, UPLOAD_FOLDER
from rag_service import answer_question, ingest_document


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        uploaded_file = request.files.get("document")

        if not uploaded_file or uploaded_file.filename == "":
            flash("Choose a PDF, TXT, or DOCX file first.", "error")
            return redirect(url_for("upload"))

        if not allowed_file(uploaded_file.filename):
            flash("Unsupported file type. Use PDF, TXT, or DOCX.", "error")
            return redirect(url_for("upload"))

        filename = secure_filename(uploaded_file.filename)
        document_id = str(uuid.uuid4())
        saved_path = Path(app.config["UPLOAD_FOLDER"]) / f"{document_id}_{filename}"
        uploaded_file.save(saved_path)

        try:
            stats = ingest_document(saved_path, filename, document_id)
        except Exception as exc:
            if saved_path.exists():
                saved_path.unlink()
            flash(f"Failed to index document: {exc}", "error")
            return redirect(url_for("upload"))

        session["document_id"] = document_id
        session["document_name"] = filename
        session["chat_history"] = []
        session["chunk_count"] = stats["chunk_count"]

        flash(f"Indexed {filename} with {stats['chunk_count']} chunks.", "success")
        return redirect(url_for("chat"))

    return render_template("upload.html", document_name=session.get("document_name"))


@app.route("/chat", methods=["GET", "POST"])
def chat():
    document_id = session.get("document_id")
    document_name = session.get("document_name")

    if not document_id:
        flash("Upload a document before asking questions.", "error")
        return redirect(url_for("upload"))

    chat_history = session.get("chat_history", [])
    answer = None
    sources = []

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if not question:
            flash("Ask a question first.", "error")
            return redirect(url_for("chat"))

        answer, sources = answer_question(document_id=document_id, question=question, history=chat_history)

        chat_history.append({"role": "user", "content": question})
        chat_history.append({"role": "assistant", "content": answer})
        session["chat_history"] = chat_history[-10:]

    return render_template(
        "chat.html",
        document_name=document_name,
        chat_history=chat_history,
        answer=answer,
        sources=sources,
        chunk_count=session.get("chunk_count", 0),
    )


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    flash("Session cleared. Upload a new document.", "success")
    return redirect(url_for("upload"))


if __name__ == "__main__":
    app.run(debug=True)