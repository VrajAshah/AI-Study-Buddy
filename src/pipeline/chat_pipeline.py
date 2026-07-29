from src.llm.base_llm import BaseLLM
from .base_pipeline import BasePipeline

class ChatPipeline(BasePipeline):

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def ask(self, question, tool_name):

        response = self.llm.generate(question)

        return response