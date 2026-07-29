from src.agent.state import AgentState
from src.context.context_builder import ContextBuilder
from src.orchestration.rule_based_decision_engine import RuleBasedDecisionEngine
from src.orchestration.workflow import Workflow
from src.pipeline.chat_pipeline import ChatPipeline
from src.pipeline.document_processing_pipeline import DocumentProcessingPipeline
from src.pipeline.tool_pipeline import ToolPipeline
from src.cleaners.text_cleaner import TextCleaner
from src.chunkers.sentence_chunker import SentenceChunker
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.retrievers.mmr_retriever import MMRRetriever
from src.prompt.prompt_builder import PromptBuilder
from src.llm.ollama_llm import Ollama
from src.llm.gemini_llm import GeminiLLM
from src.indexing.document_indexing import DocumentIndexer
from src.pipeline.rag_pipeline import RAGPipeline
from src.rerankers.NoOpReranker import NoOpReranker
from src.memory.conversation_memory import ConversationMemory
from src.memory_managers.recent_memory_manager import RecentMemoryManager
from src.tools.calculator_tool import CalculatorTool
from src.tools.registry import ToolRegistry
from src.tools.executor import ToolExecutor
from src.tools.parser import ToolParser
from src.agent.intelligent_agent import IntelligentAgent
from src.workflows.rag_workflow import RAGWorkFlow
from src.workflows.chat_workflow import ChatWorkFlow
from src.workflows.tool_workflow import ToolWorkflow
from src.orchestration.workflow_registry import WorkFlowRegistry
from src.store.in_memory_store import InMemoryDocumentStore

from dotenv import load_dotenv
import os

class AgentFactory:

    @staticmethod
    def create():
        try:
            generator = EmbeddingGenerator()

            load_dotenv()

            api_key = os.getenv("GEMINI_API_KEY")

            # llm = Ollama("gemma3:1b")
            llm = GeminiLLM(api_key=os.getenv("GEMINI_API_KEY"))

            memory = ConversationMemory()

            memory_manager = RecentMemoryManager()

            prompt_builder = PromptBuilder()

            reranker = NoOpReranker()

            indexer = DocumentIndexer(
                embedding_generator=generator,
                cleaner=TextCleaner(),
                chunker=SentenceChunker()
            )

            retriever = MMRRetriever(generator)

            parser = ToolParser()

            registry = ToolRegistry()

            registry.register(CalculatorTool())

            executor = ToolExecutor(registry)

            store = InMemoryDocumentStore()

            state = AgentState()

            state.available_tools = [ tool.name for tool in registry.list_tools() ]

            document_pipeline = DocumentProcessingPipeline(indexer=indexer,store=store,state=state)

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
                llm=llm,
                parser=parser,
                executor=executor
            )

            chat_workflow = ChatWorkFlow(chat_pipeline)

            rag_workflow = RAGWorkFlow(rag_pipeline)

            tool_workflow = ToolWorkflow(tool_pipeline)


            workflow_registry = WorkFlowRegistry()

            workflow_registry.register(
                Workflow.CHAT,
                chat_workflow
            )

            workflow_registry.register(
                Workflow.RAG,
                rag_workflow
            )

            workflow_registry.register(
                Workflow.TOOL,
                tool_workflow
            )

            context_builder = ContextBuilder()

            decision_engine = RuleBasedDecisionEngine()

            return IntelligentAgent(
                state=state,
                context_builder=context_builder,
                decision_engine=decision_engine,
                workflow_registry=workflow_registry,
                document_processing_pipeline=document_pipeline
            )

        except Exception as e:
            print("ERROR -*-*-*", e)