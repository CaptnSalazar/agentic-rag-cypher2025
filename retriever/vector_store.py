from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from typing import List, Dict

class SimpleVectorStore:
    def __init__(self, model_name='all-MiniLM-L6-v2', index_path='./vector.index'):
        self.model = SentenceTransformer(model_name)
        self.index_path = index_path
        self.dim = self.model.get_sentence_embedding_dimension()
        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            self.metadatas = self._load_meta(index_path + '.meta')
        else:
            self.index = faiss.IndexFlatIP(self.dim)
            self.metadatas = []

    def _load_meta(self, path):
        import json
        if os.path.exists(path):
            return json.load(open(path, 'r'))
        return []

    def _save_meta(self, path):
        import json
        json.dump(self.metadatas, open(path, 'w'))

    def add(self, docs: List[Dict]):
        texts = [d['text'] for d in docs]
        emb = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        self.index.add(emb)
        self.metadatas.extend(docs)
        self._save_meta(self.index_path + '.meta')

    def query(self, text: str, top_k: int = 5):
        emb = self.model.encode([text], convert_to_numpy=True, normalize_embeddings=True)
        D, I = self.index.search(emb, top_k)
        results = []
        for idx in I[0]:
            if idx < len(self.metadatas):
                results.append(self.metadatas[idx])
        return results