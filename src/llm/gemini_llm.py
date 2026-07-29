from google import genai

from src.llm.base_llm import BaseLLM
from src.models.llm_response import LLMResponse
from src.models.token_usage import TokenUsage


class GeminiLLM(BaseLLM):

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-3.6-flash"
    ):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> LLMResponse:

        interaction = self.client.interactions.create(
            model=self.model,
            input=prompt
        )

        return self._map_response(interaction)

    def _map_response(self, interaction):

        usage = TokenUsage(
            prompt_tokens=interaction.usage.total_input_tokens,
            completion_tokens=interaction.usage.total_output_tokens,
        )

        return LLMResponse(
            content=interaction.output_text,
            model_name=interaction.model,
            usage=usage,
            response_time=None,
            finish_reason=interaction.status,
            created_at=interaction.created,
        )