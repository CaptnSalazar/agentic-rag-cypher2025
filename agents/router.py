from enum import Enum

class QueryType(Enum):
    FACTUAL = 'factual'
    OPEN = 'open'
    REASON = 'reasoning'

class QueryRouter:
    def __init__(self):
        pass

    def classify(self, text: str) -> QueryType:
        t = text.lower()
        if any(w in t for w in ['why', 'how', 'calculate', 'prove', 'reason']):
            return QueryType.REASON
        if any(w in t for w in ['compare', 'pros', 'cons', 'opinions', 'best', 'recommend']):
            return QueryType.OPEN
        return QueryType.FACTUAL