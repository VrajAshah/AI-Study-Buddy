class ToolRegistry():

    def __init__(self):
        self._tools = {}

    def register(self, tool):
        self._tools[tool.name] = tool

    def get_tool(self, name):
        return self._tools.get(name)

    def check_tool(self, name):
        return name in self._tools

    def list_tools(self):
        return list(self._tools.values())