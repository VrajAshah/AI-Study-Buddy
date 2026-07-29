from .base_decision_engine import BaseDecisionEngine
from .decision import Decision
from .workflow import Workflow
import re

class RuleBasedDecisionEngine(BaseDecisionEngine):

    def decide(self, context):

        if self._should_use_rag(context):
            return Decision(workflow=Workflow.RAG,confidence=0.95,reason="Document detected", tool_name="rag")
        elif self._is_tool_request(context):
            return Decision(workflow=Workflow.TOOL,confidence=0.95,reason="Arithmetic operation detected", tool_name="calculator")
        else:
            return Decision(workflow=Workflow.CHAT,confidence=0.95,reason="No related tool/document detected", tool_name="chat")

    def _should_use_rag(self, context):

        if not context.has_active_document:
            return False

        if self._is_tool_request(context):
            return False

        return True


    def _is_document_related(self, context):

        return False

    def _is_tool_request(self, context):

        return (re.fullmatch(r"[-+]?\d+(\s*[-+*/]\s*[-+]?\d+)*",context.question.strip()) is not None)