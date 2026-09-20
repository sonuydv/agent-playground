import numpy as np


class VectorStore:

    def __init__(self):
        self.documents = []
        self.vectors = []

    def add(self, documents: list[str], vectors: list[list[float]]):

        self.documents.extend(documents)
        self.vectors.extend(vectors)

    def search(self, query_vector: list[float], top_k: int = 3):

        query = np.array(query_vector)

        scores = []

        for document, vector in zip(self.documents, self.vectors):

            vector = np.array(vector)

            similarity = np.dot(query, vector) / (
                np.linalg.norm(query) * np.linalg.norm(vector)
            )

            scores.append(
                {
                    "document": document,
                    "score": float(similarity),
                }
            )

        scores.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return scores[:top_k]