from src.tools.base_tool import BaseTool

class CalculatorTool(BaseTool):

    @property
    def name(self):
        return "calculator"

    @property
    def description(self):
        return ("Performs arithmetic calculations. " "Supports +, -, *, /, %, ** and parentheses.")

    def execute(self, expression):
        try:
            result = eval(
                expression,
                {"__builtins__": {}},   # Disable built-in functions
                {}
            )

            return {
                "expression": expression,
                "result": result
            }

        except Exception as e:
            return {
                "error": str(e)
            }