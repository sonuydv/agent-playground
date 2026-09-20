from agent_demo.rag.generator import generate_answer
from agent_demo.rag.loader import load_document
from agent_demo.rag.chunker import chunk_text
from agent_demo.rag.embeddings import embed_texts
from agent_demo.rag.retriever import Retriever
from agent_demo.rag.vector_store import VectorStore


def main():

    # 1. Load
    text = load_document("data/documents/company.txt")

    # 2. Chunk
    chunks = chunk_text(text)

    print("\nCHUNKS:\n")

    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i} ---")
        print(chunk)

    # 3. Embed
    vectors = embed_texts(chunks)

    print("\nEmbedding dimension:", len(vectors[0]))

    # 4. Store
    vector_store = VectorStore()

    vector_store.add(
        documents=chunks,
        vectors=vectors,
    )

    # 5. Retrieve
    retriever = Retriever(vector_store)

    query = "How many vacation days do employees get?"

    results = retriever.retrieve(query, top_k=2)

    retrieved_documents = [
        result["document"]
        for result in results
    ]

    answer = generate_answer(
        question=query,
        retrieved_documents=retrieved_documents,
    )

    print("\nANSWER:\n")
    print(answer)


if __name__ == "__main__":
    main()