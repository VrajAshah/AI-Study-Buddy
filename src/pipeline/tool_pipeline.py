from src.models.tool_call import ToolCall

from .base_pipeline import BasePipeline
class ToolPipeline(BasePipeline):

    def __init__(self, llm, parser, executor):
        self.llm = llm
        self.parser = parser
        self.executor = executor

    def ask(self, question, tool_name):

        tool_call = ToolCall(
            name=tool_name,
            arguments={
                "expression": question
            }
        )

        result = self.executor.execute(tool_call)

        return result