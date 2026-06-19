from pinecone import Pinecone, ServerlessSpec

from config import PINECONE_API_KEY, PINECONE_CLOUD, PINECONE_INDEX_NAME, PINECONE_REGION


if not PINECONE_API_KEY:
    raise RuntimeError("PINECONE_API_KEY is missing from the environment")


pc = Pinecone(api_key=PINECONE_API_KEY)


def ensure_index() -> None:
    existing_indexes = pc.list_indexes().names()

    if PINECONE_INDEX_NAME in existing_indexes:
        return

    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud=PINECONE_CLOUD, region=PINECONE_REGION),
    )


def get_index():
    ensure_index()
    return pc.Index(PINECONE_INDEX_NAME)