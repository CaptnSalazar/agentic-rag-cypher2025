import re
from typing import List, Dict

class Verifier:
    def __init__(self):
        pass

    def verify_claims(self, claim: str, sources: List[Dict]) -> Dict:
        support = []
        for s in sources:
            text = s.get('text','')
            if claim.lower() in text.lower():
                support.append({'source': s.get('source_id'), 'evidence_excerpt': text[:200]})
        confidence = min(0.99, 0.2 + 0.2 * len(support))
        return {'claim': claim, 'supported_by': support, 'confidence': confidence}