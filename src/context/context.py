from dataclasses import dataclass

@dataclass
class Context:

    has_active_document: bool
    has_history: bool
    tools_available: list[str]
    question: str
     
