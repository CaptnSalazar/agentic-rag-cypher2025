import json
from retriever.vector_store import SimpleVectorStore


if __name__ == "__main__":
    vs = SimpleVectorStore()
    sample_docs = [
    {"text": "Server crashes are often caused by memory leaks or misconfigured cron jobs.", "source_id": "doc1", "url": None, "trust_score": 0.7},
    {"text": "RAG systems combine retrieval with generation to reduce hallucinations.", "source_id": "doc2", "url": None, "trust_score": 0.8}
    ]
    vs.add(sample_docs)
    print("Sample documents ingested and index saved.")