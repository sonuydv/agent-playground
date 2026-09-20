from agent_demo.rag.embeddings import embed_text
from agent_demo.rag.vector_store import VectorStore


class Retriever:

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 3):

        query_vector = embed_text(query)

        return self.vector_store.search(
            query_vector,
            top_k=top_k,
        )