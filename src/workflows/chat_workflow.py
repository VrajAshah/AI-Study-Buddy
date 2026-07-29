from .base_workflow import BaseWorkflow
from src.pipeline.chat_pipeline import ChatPipeline

class ChatWorkFlow(BaseWorkflow):

    def __init__(self, pipeline: ChatPipeline):
        self.pipeline = pipeline

    def execute(self, context, decision):
        return self.pipeline.ask(context.question,tool_name = decision.tool_name)