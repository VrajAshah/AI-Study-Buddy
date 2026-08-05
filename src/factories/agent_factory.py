from src.agent.intelligent_agent import IntelligentAgent
from src.agent.state import AgentState

from src.context.context_builder import ContextBuilder

from src.document_manager.document_manager import DocumentManager
from src.factories.prompt_factory import PromptFactory
from src.orchestration.rule_based_decision_engine import RuleBasedDecisionEngine

from src.orchestration.workflow import Workflow
from src.pipeline.chat_pipeline import ChatPipeline
from src.pipeline.document_processing_pipeline import DocumentProcessingPipeline
from src.pipeline.rag_pipeline import RAGPipeline
from src.pipeline.tool_pipeline import ToolPipeline

from src.factories.llm_factory import LLMFactory
from src.factories.memory_factory import MemoryFactory
from src.factories.processing_factory import ProcessingFactory
from src.factories.retriever_factory import RetrieverFactory
from src.factories.store_factory import StoreFactory
from src.factories.tool_factory import ToolFactory
from src.factories.workflow_factory import WorkflowFactory
from src.logging.logging import get_logger

logger = get_logger(__name__)


class AgentFactory:

    @staticmethod
    def create():
        try:

            # ---------- Processing ----------
            embedding_generator = ProcessingFactory.create_embedding_generator()

            indexer = ProcessingFactory.create_indexer(
                embedding_generator
            )

            # prompt_builder = ProcessingFactory.create_prompt_builder()
            prompt_builder = PromptFactory.create(Workflow.RAG)

            reranker = ProcessingFactory.create_reranker()

            # ---------- LLM ----------
            llm = LLMFactory.create()

            # ---------- Retrieval ----------
            retriever = RetrieverFactory.create(
                embedding_generator
            )

            # ---------- Memory ----------
            memory = MemoryFactory.create_memory()

            memory_manager = MemoryFactory.create_manager()

            # ---------- Store ----------
            store = StoreFactory.create()

            # ---------- Tools ----------
            registry = ToolFactory.create_registry()

            executor = ToolFactory.create_executor(
                registry
            )

            # ---------- Agent State ----------
            state = AgentState()

            state.available_tools = [
                tool.name
                for tool in registry.list_tools()
            ]

            # ---------- Pipelines ----------
            document_pipeline = DocumentProcessingPipeline(
                indexer=indexer,
                store=store,
                state=state
            )

            document_manager = DocumentManager(
                document_pipeline,
                state
            )

            chat_pipeline = ChatPipeline(
                llm=llm
            )

            rag_pipeline = RAGPipeline(
                retriever=retriever,
                reranker=reranker,
                prompt_builder=prompt_builder,
                llm=llm,
                memory=memory,
                memory_manager=memory_manager,
                store=store
            )

            tool_pipeline = ToolPipeline(
                executor=executor
            )

            # ---------- Workflow Registry ----------
            workflow_registry = WorkflowFactory.create(
                chat_pipeline=chat_pipeline,
                rag_pipeline=rag_pipeline,
                tool_pipeline=tool_pipeline
            )

            # ---------- Agent ----------
            return IntelligentAgent(
                state=state,
                context_builder=ContextBuilder(),
                decision_engine=RuleBasedDecisionEngine(),
                workflow_registry=workflow_registry,
                document_manager=document_manager
            )

        except Exception as e:
            logger.error("Error in agent factory " + str(e))
            logger.exception(e)