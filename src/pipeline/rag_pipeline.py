from src.indexing.document_indexing import DocumentIndexer
from src.retrievers.base_retriever import BaseRetriever
from src.prompt.base_prompt_builder import BasePromptBuilder
from src.llm.base_llm import BaseLLM
from src.store.in_memory_store import InMemoryDocumentStore
from src.config.document_rules import PROMPT_CHUNK_SIZE
from src.rerankers.NoOpReranker import NoOpReranker
from src.rerankers.BaseReranker import BaseReranker
from src.memory.base_memory import BaseMemory
from src.memory_managers.base_memory_manager import BaseMemoryManager
from .base_pipeline import BasePipeline
from src.config.settings import settings
from src.prompt.prompt_context import PromptContext

from src.logging.logging import get_logger

logger = get_logger(__name__)

class RAGPipeline(BasePipeline):

    def __init__(
        self,
        retriever: BaseRetriever,
        reranker: BaseReranker,
        prompt_builder: BasePromptBuilder,
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
        try:

            history = self.memory_manager.get_context(self.memory, question)

            self.memory.add_message("user", question)

            retrieval_results = self.retriever.retrieve(
                self.store,
                question,
                top_k=settings.retriever.top_k
            )

            retrieval_results = self.reranker.rerank(
                question,
                retrieval_results,
                top_k=settings.retriever.rerank_top_k
            )

            prompt_context = PromptContext(
                question=question,
                history=history,
                retrieval_results=retrieval_results
            )

            prompt = self.prompt_builder.build(prompt_context)

            if retrieval_results:
                response = self.llm.generate(prompt)

            else:
                response = ""

            self.memory.add_message("assistant", response)

            return response

        except Exception as e:
            logger.error("Error in RAG pipeline " + str(e))
            logger.exception(e)
