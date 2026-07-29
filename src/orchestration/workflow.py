from enum import Enum

class Workflow(Enum):

    CHAT = "chat"
    RAG = "rag"
    TOOL = "tool"
    DOCUMENT = "document"