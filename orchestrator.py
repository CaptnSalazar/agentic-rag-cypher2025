from agents.router import QueryRouter, QueryType
from retriever.vector_store import SimpleVectorStore
from agents.web_search import WebSearchAgent
from agents.ranker_qa import RankerQA
from agents.reasoner import Reasoner
from agents.verifier import Verifier
from llm_clients.openai_client import OpenAIClient

class AgenticRAG:
    def __init__(self):
        self.router = QueryRouter()
        self.vs = SimpleVectorStore()
        self.web = WebSearchAgent()
        self.llm = OpenAIClient()
        self.ranker = RankerQA(llm_client=self.llm)
        self.reasoner = Reasoner(llm=self.llm)
        self.verifier = Verifier()

    def handle(self, query: str) -> dict:
        qtype = self.router.classify(query)
        print(f"[router] classified query as: {qtype}")

        docs = []
        if qtype == QueryType.FACTUAL:
            docs = self.vs.query(query, top_k=5)
            web = self.web.search(query, num=3)
            docs.extend(web)
        elif qtype == QueryType.OPEN:
            # broaden web + local
            web = self.web.search(query, num=8)
            docs = self.vs.query(query, top_k=3) + web
        else:  # reasoning
            docs = self.vs.query(query, top_k=10)
            docs += self.web.search(query, num=5)

        qa = self.ranker.extractive_answer(query, docs, top_n=4)
        if qtype == QueryType.REASON:
            reason = self.reasoner.reason(query, [d.get('text','') for d in docs[:4]])
            qa['reasoning'] = reason

        verification = self.verifier.verify_claims(qa['answer'] if isinstance(qa['answer'], str) else str(qa), docs[:4])
        qa['verification'] = verification

        qa['provenance'] = [{ 'source_id': d.get('source_id','local'), 'url': d.get('url'), 'trust_score': d.get('trust_score', 0.5)} for d in docs[:6]]
        return qa


if __name__ == '__main__':
    ag = AgenticRAG()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--mode', default='auto')
    args = parser.parse_args()
    out = ag.handle(args.query)
    import json
    print(json.dumps(out, indent=2))