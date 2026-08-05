from dataclasses import dataclass

@dataclass
class LLMConfig:

    provider: str = "gemini"
    model: str = "gemini-3.6-flash"
    temperature: float = 0.0
    max_tokens: int = 2048