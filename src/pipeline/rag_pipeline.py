from src.indexing.document_indexing import DocumentIndexer
from src.retrievers.base_retriever import BaseRetriever
from src.prompt.prompt_builder import PromptBuilder
from src.llm.base_llm import BaseLLM
from src.store.in_memory_store import InMemoryDocumentStore
from src.config.document_rules import PROMPT_CHUNK_SIZE
from src.rerankers.NoOpReranker import NoOpReranker
from src.rerankers.BaseReranker import BaseReranker
from src.memory.base_memory import BaseMemory
from src.memory_managers.base_memory_manager import BaseMemoryManager
from .base_pipeline import BasePipeline

class RAGPipeline(BasePipeline):

    def __init__(
        self,
        retriever: BaseRetriever,
        reranker: BaseReranker,
        prompt_builder: PromptBuilder,
        llm: BaseLLM,
        memory: BaseMemory,
        memory_manager: BaseMemoryManager,
        store: InMemoryDocumentStore
    ):
        self.retriever = retriever
        self.reranker = reranker
        self.prompt_builder = prompt_builder
        self.llm = llm
        self.memory = memory
        self.memory_manager = memory_manager

        self.document = None
        self.store = store

    def ask(self, question, tool_name):

        history = self.memory_manager.get_context(self.memory, question)

        self.memory.add_message("user", question)

        retrieval_results = self.retriever.retrieve(
            self.store,
            question,
            top_k=20
        )

        retrieval_results = self.reranker.rerank(
            question,
            retrieval_results,
            top_k=3
        )

        prompt = self.prompt_builder.build(
            question,
            retrieval_results,
            history
        )

        if retrieval_results:
            response = self.llm.generate(prompt)

        else:
            response = ""

        self.memory.add_message("assistant", response)

        return response