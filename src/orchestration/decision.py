from dataclasses import dataclass
from typing import Optional
from .workflow import Workflow

@dataclass
class Decision:

    workflow: Workflow
    confidence: float = 1.0
    reason: str = ""

    tool_name: Optional[str]= None