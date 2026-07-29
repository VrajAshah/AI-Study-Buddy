from dataclasses import dataclass

@dataclass
class ToolCall:

    name: str
    arguments: dict