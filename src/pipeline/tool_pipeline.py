from src.models.tool_call import ToolCall

from .base_pipeline import BasePipeline

from src.logging.logging import get_logger

logger = get_logger(__name__)

class ToolPipeline(BasePipeline):

    def __init__(self, executor):
        self.executor = executor

    def ask(self, question, tool_name):
        try:
            tool_call = ToolCall(
                name=tool_name,
                arguments={
                    "expression": question
                }
            )

            result = self.executor.execute(tool_call)

            return result
        except Exception as e:
            logger.error("Error in tool pipeline " + str(e))
            logger.exception(e)