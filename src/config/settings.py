from .llm_config import LLMConfig
from .document_rules import DOCUMENT_RULES
from .document_config import DocumentConfig
from .logging_config import LoggingConfig
from .memory_config import MemoryConfig
from .retriever_config import RetrieverConfig

class Configuration:

    def __init__(self):
        self.llm = LLMConfig()
        self.retriever = RetrieverConfig()
        self.memory = MemoryConfig()
        self.document = DocumentConfig()
        self.logging = LoggingConfig()


settings = Configuration()