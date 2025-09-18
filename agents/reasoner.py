from typing import List, Dict

class Reasoner:
    def __init__(self, llm=None, show_steps=True):
        self.llm = llm
        self.show_steps = show_steps

    def reason(self, question: str, evidence: List[str]) -> Dict:
        # evidence: list of text strings
        steps = []
        steps.append("Step 1: Extract key facts from evidence.")
        steps.append("Step 2: Lay out assumptions and constraints.")
        steps.append("Step 3: Apply logical chain to reach conclusion.")
        conclusion = "Based on evidence, probable cause is X (hypothetical)."
        return {'steps': steps if self.show_steps else None, 'conclusion': conclusion}