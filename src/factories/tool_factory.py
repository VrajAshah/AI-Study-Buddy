from src.tools.registry import ToolRegistry
from src.tools.executor import ToolExecutor
from src.tools.calculator_tool import CalculatorTool

class ToolFactory:

    @staticmethod
    def create_registry():

        registry = ToolRegistry()

        registry.register(
            CalculatorTool()
        )

        return registry

    @staticmethod
    def create_executor(registry):

        return ToolExecutor(
            registry
        )