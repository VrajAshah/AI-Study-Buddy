import json 
from src.models.tool_call import ToolCall

class ToolParser:

    def parse(self, response):

        data = json.loads(response)

        return ToolCall(name=data["tool"], arguments= data["arguments"])