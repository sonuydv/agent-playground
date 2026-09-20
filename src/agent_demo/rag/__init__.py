from agent_demo.rag.chunker import chunk_text
from agent_demo.rag.embeddings import embed_texts
from agent_demo.rag.loader import load_document
from agent_demo.rag.retriever import Retriever
from agent_demo.rag.vector_store import VectorStore


text = load_document("data/documents/company.txt")

chunks = chunk_text(text)

vectors = embed_texts(chunks)

vector_store = VectorStore()

vector_store.add(chunks, vectors)

retriever = Retriever(vector_store)

