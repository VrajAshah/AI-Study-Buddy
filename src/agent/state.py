from dataclasses import dataclass, field

@dataclass
class AgentState:

    active_documents: list[str] = field(default_factory=list)
    conversation_history: list[str] = field(default_factory=list)
    available_tools: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def add_document(self, document: str):
        self.active_documents.append(document)

    def remove_document(self, document: str):
        self.active_documents.remove(document)

    def clear_documents(self):
        self.active_documents.clear()

