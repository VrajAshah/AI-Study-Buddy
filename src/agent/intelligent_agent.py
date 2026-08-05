from .base_agent import BaseAgent
from src.context.context_builder import ContextBuilder
from src.orchestration.base_decision_engine import BaseDecisionEngine
from src.orchestration.workflow_registry import WorkFlowRegistry
from src.agent.state import AgentState

from src.logging.logging import get_logger

logger = get_logger(__name__)

class IntelligentAgent(BaseAgent):

    def __init__(
                    self, 
                    state: AgentState,
                    context_builder: ContextBuilder, 
                    decision_engine: BaseDecisionEngine, 
                    workflow_registry: WorkFlowRegistry,
                    document_manager
                ):

        self.state = state
        self.context_builder = context_builder
        self.decision_engine = decision_engine
        self.workflow_registry = workflow_registry
        self.document_manager = document_manager

    def run(self, question):

        try:

            context = self.context_builder.build(question, self.state)

            decision = self.decision_engine.decide(context)

            workflow = self.workflow_registry.get(decision.workflow)

            response = workflow.execute(context, decision)

            return response

        except Exception as e:
            logger.error("Error in intelligent agent " + str(e))
            logger.exception(e)

    def process_document(self, document):

        return self.document_manager.process_document(document)