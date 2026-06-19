from pathlib import Path

from pypdf import PdfReader


def load_document_text(file_path: Path) -> str:
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf_text(file_path)

    if suffix == ".docx":
        return load_docx_text(file_path)

    return file_path.read_text(encoding="utf-8", errors="ignore")


def load_pdf_text(file_path: Path) -> str:
    reader = PdfReader(str(file_path))
    parts = []

    for page in reader.pages:
        extracted = page.extract_text() or ""
        if extracted.strip():
            parts.append(extracted.strip())

    return "\n".join(parts)


def load_docx_text(file_path: Path) -> str:
    try:
        from docx import Document
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "DOCX support requires the python-docx package. Install the requirements in the same environment you use to run the app."
        ) from exc

    document = Document(str(file_path))
    parts = [paragraph.text.strip() for paragraph in document.paragraphs if paragraph.text.strip()]
    return "\n".join(parts)


def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 150) -> list[str]:
    cleaned = " ".join(text.split())

    if not cleaned:
        return []

    words = cleaned.split(" ")
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))

        if end == len(words):
            break

        start = max(end - chunk_overlap, start + 1)

    return chunks