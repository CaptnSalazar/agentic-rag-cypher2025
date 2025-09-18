from typing import List, Dict

class RankerQA:
    def __init__(self, llm_client=None):
        self.llm = llm_client

    def extractive_answer(self, question: str, docs: List[Dict], top_n=3) -> Dict:

        context = '\n\n'.join([f"[{d.get('source_id','')}] {d.get('text','')}" for d in docs[:top_n]])
        prompt = f"Answer the question using ONLY the context below. If answer not present, say 'not found'.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
        if self.llm:
            resp = self.llm.complete(prompt)
            return {'answer': resp, 'provenance': [d.get('source_id') for d in docs[:top_n]]}

        combined = ' '.join([d.get('text','') for d in docs[:top_n]])
        return {'answer': combined[:800], 'provenance': [d.get('source_id') for d in docs[:top_n]]}