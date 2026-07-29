from src.agent.base_agent import BaseAgent

class ToolCallingAgent(BaseAgent):

    def __init__(self,pipeline,parser,executor):

        self.pipeline = pipeline
        self.parser = parser
        self.executor = executor

    def run(self, question: str):

        response = self.pipeline.ask(question)

        parsed = self.parser.parse(response.content)

        if parsed.tool_call:

            result = self.executor.execute(parsed.tool_call)

        return response.content