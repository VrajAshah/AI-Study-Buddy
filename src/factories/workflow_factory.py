from src.orchestration.workflow import Workflow
from src.orchestration.workflow_registry import WorkFlowRegistry
from src.workflows.chat_workflow import ChatWorkFlow
from src.workflows.rag_workflow import RAGWorkFlow
from src.workflows.tool_workflow import ToolWorkflow

class WorkflowFactory:

    @staticmethod
    def create(
        chat_pipeline,
        rag_pipeline,
        tool_pipeline,
    ):

        registry = WorkFlowRegistry()

        registry.register(
            Workflow.CHAT,
            ChatWorkFlow(chat_pipeline)
        )

        registry.register(
            Workflow.RAG,
            RAGWorkFlow(rag_pipeline)
        )

        registry.register(
            Workflow.TOOL,
            ToolWorkflow(tool_pipeline)
        )

        return registry