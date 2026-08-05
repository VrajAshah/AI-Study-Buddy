from src.prompt.chat_prompt_builder import ChatPromptBuilder
from src.prompt.rag_prompt_builder import RAGPromptBuilder
from src.prompt.tool_prompt_builder import ToolPromptBuilder
from src.orchestration.workflow import Workflow

class PromptFactory:

    @staticmethod
    def create(workflow: Workflow):

        if workflow == Workflow.CHAT:
            return ChatPromptBuilder()

        elif workflow == Workflow.RAG:
            return RAGPromptBuilder()

        elif workflow == Workflow.TOOL:
            return ToolPromptBuilder()

        raise ValueError(
            f"Unknown prompt builder: {workflow}"
        )