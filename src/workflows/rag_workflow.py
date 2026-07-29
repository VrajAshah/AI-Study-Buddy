from .base_workflow import BaseWorkflow
from src.pipeline.rag_pipeline import RAGPipeline

class RAGWorkFlow(BaseWorkflow):

    def __init__(self, pipeline: RAGPipeline):
        self.pipeline = pipeline

    def execute(self, context, decision):
        return self.pipeline.ask(context.question,tool_name = decision.tool_name)