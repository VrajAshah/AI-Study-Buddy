from ollama import Client
from src.llm.base_llm import BaseLLM
from src.models.llm_response import LLMResponse
from src.models.token_usage import TokenUsage

class Ollama(BaseLLM):

    def __init__(self, model_name,host: str = "http://localhost:11434"):
        self.model_name = model_name
        self.client = Client(host=host)

    def generate(self, prompt):

        raw_response = self.client.chat(
            model = self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return self._map_response(raw_response)

    def _map_response(self, raw_response):

        return LLMResponse(
            content=raw_response.message.content,
            model_name=raw_response.model,
            usage=TokenUsage(
                prompt_tokens=raw_response.prompt_eval_count,
                completion_tokens=raw_response.eval_count,
            ),
            response_time=raw_response.total_duration / 1000000000,
            finish_reason=raw_response.done_reason,
            created_at=raw_response.created_at,
        )
