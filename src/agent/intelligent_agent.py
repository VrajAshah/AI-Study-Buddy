from .base_agent import BaseAgent
from src.context.context_builder import ContextBuilder
from src.orchestration.base_decision_engine import BaseDecisionEngine
from src.orchestration.workflow_registry import WorkFlowRegistry
from src.agent.state import AgentState

class IntelligentAgent(BaseAgent):

    def __init__(
                    self, 
                    state: AgentState,
                    context_builder: ContextBuilder, 
                    decision_engine: BaseDecisionEngine, 
                    workflow_registry: WorkFlowRegistry,
                    document_processing_pipeline
                ):

        self.state = state
        self.context_builder = context_builder
        self.decision_engine = decision_engine
        self.workflow_registry = workflow_registry
        self.document_processing_pipeline = document_processing_pipeline

    def run(self, question):

        context = self.context_builder.build(question, self.state)

        decision = self.decision_engine.decide(context)

        workflow = self.workflow_registry.get(decision.workflow)

        response = workflow.execute(context, decision)

        return response

    def process_document(self, document):

        return self.document_processing_pipeline.process(document)