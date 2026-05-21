from typing import List

import numpy as np

from sentence_transformers import SentenceTransformer


class HFEmbeddings:

    def __init__(self):

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    # -----------------------------------------------------
    # EMBED DOCUMENTS
    # -----------------------------------------------------

    def embed_documents(
        self,
        texts: List[str]
    ) -> np.ndarray:

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.astype("float32")

    # -----------------------------------------------------
    # EMBED QUERY
    # -----------------------------------------------------

    def embed_query(
        self,
        text: str
    ) -> np.ndarray:

        embedding = self.model.encode(
            [text],
            convert_to_numpy=True
        )

        return embedding.astype("float32")