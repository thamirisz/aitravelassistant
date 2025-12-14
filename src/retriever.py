from src.embeddings import get_embeddings
from src.config import COLLECTION_NAME
from src.vectorstores import get_qdrant_client
from importlib.metadata import version

def retrieve_docs(query: str, top_k=5):
    client = get_qdrant_client()

    query_vector = get_embeddings([query])[0]

    print("Qdrant client version:", version("qdrant-client"))

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True
    )

    hits = search_result.points  # ✅ THIS is the list

    return [
        hit.payload.get("text", "")
        for hit in hits
        if hit.payload and "text" in hit.payload
    ]
