from dataclasses import dataclass, field
from typing import Any

@dataclass
class PromptContext:

    question: str

    history: list = field(default_factory=list)

    retrieval_results: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    extras: dict[str, Any] = field(default_factory=dict)