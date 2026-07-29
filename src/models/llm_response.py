from dataclasses import dataclass, field
from typing import Optional

from src.models.tool_call import ToolCall
from src.models.token_usage import TokenUsage


@dataclass
class LLMResponse:

    content: Optional[str] = None
    tool_call: Optional[ToolCall] = None
    model_name: Optional[str] = None
    usage: Optional[TokenUsage] = None
    response_time: Optional[float] = None
    finish_reason: Optional[str] = None
    created_at: Optional[str] = None