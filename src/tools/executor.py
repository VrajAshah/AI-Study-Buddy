class ToolExecutor():

    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_call):

        tool = self.registry.get_tool(tool_call.name)

        if tool is None:
            raise ValueError(f"Tool '{tool_call.name}' not found.")

        try:
            return tool.execute(**tool_call.arguments)

        except Exception as e:
            return {"status": "error", "message": str(e)}