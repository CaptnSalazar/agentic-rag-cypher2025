from dataclasses import dataclass, asdict

@dataclass
class Provenance:
    source_id: str
    title: str | None
    url: str | None
    retrieval_method: str
    trust_score: float

    def to_dict(self):
        return asdict(self)