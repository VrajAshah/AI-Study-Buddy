from .base_workflow import BaseWorkflow

class ToolWorkflow(BaseWorkflow):

    def __init__(self, pipeline):
        self.pipeline = pipeline

    def execute(self, context, decision):
        return self.pipeline.ask(context.question, tool_name = decision.tool_name)