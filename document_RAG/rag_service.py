from config import CHUNK_OVERLAP, CHUNK_SIZE, MAX_HISTORY_MESSAGES, TOP_K
from document_utils import chunk_text, load_document_text
from embeddings import embed_query, embed_texts
from llm import generate_answer
from pinecone_store import get_index


def ingest_document(file_path, original_name: str, document_id: str) -> dict:
    text = load_document_text(file_path)
    chunks = chunk_text(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    if not chunks:
        raise ValueError("The document does not contain readable text.")

    index = get_index()
    vectors = embed_texts(chunks)

    records = []
    for position, (chunk, vector) in enumerate(zip(chunks, vectors), start=1):
        records.append(
            {
                "id": f"{document_id}-{position}",
                "values": vector,
                "metadata": {
                    "text": chunk,
                    "source": original_name,
                    "chunk_number": position,
                },
            }
        )

    index.upsert(vectors=records, namespace=document_id)

    return {"chunk_count": len(chunks)}


def answer_question(document_id: str, question: str, history: list[dict] | None = None) -> tuple[str, list[dict]]:
    index = get_index()
    question_vector = embed_query(question)

    results = index.query(
        namespace=document_id,
        vector=question_vector,
        top_k=TOP_K,
        include_metadata=True,
    )

    matches = results.get("matches", []) if isinstance(results, dict) else getattr(results, "matches", [])
    context_blocks = []
    sources = []

    for match in matches:
        metadata = match.get("metadata", {}) if isinstance(match, dict) else getattr(match, "metadata", {})
        text = metadata.get("text", "")
        source = metadata.get("source", "document")
        chunk_number = metadata.get("chunk_number", 0)
        score = match.get("score", 0.0) if isinstance(match, dict) else getattr(match, "score", 0.0)

        if text:
            context_blocks.append(f"Source: {source} | Chunk {chunk_number}\n{text}")
            sources.append({"source": source, "chunk_number": chunk_number, "score": round(float(score), 4)})

    recent_history = history[-MAX_HISTORY_MESSAGES:] if history else []
    history_text = "\n".join(
        f"{item['role'].title()}: {item['content']}" for item in recent_history if item.get("content")
    )

    system_prompt = (
        "You are a precise document question-answering assistant. "
        "Answer only from the provided context. If the answer is not in the context, say you cannot find it in the uploaded document. "
        "Keep the answer concise, correct, and helpful."
    )

    user_prompt = f"""
Document context:
{chr(10).join(context_blocks) if context_blocks else 'No relevant context was found.'}

Conversation history:
{history_text if history_text else 'None'}

Question:
{question}

Answer with a short explanation and, when helpful, mention which chunk(s) support the answer.
""".strip()

    answer = generate_answer(system_prompt=system_prompt, user_prompt=user_prompt)
    return answer, sources