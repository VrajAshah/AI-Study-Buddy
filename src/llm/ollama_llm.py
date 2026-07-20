from ollama import Client
from src.llm.base_llm import BaseLLM
from src.models.llm_response import LLMResponse

class Ollama(BaseLLM):

    def __init__(self, model_name,host: str = "http://localhost:11434"):
        self.model_name = model_name
        self.client = Client(host=host)

    def generate(self, prompt):
        print("generate -------Ollama--->>>")

        raw_response = self.client.chat(
            model = self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print("raw_response ---------->>>", raw_response)
        # return raw_response
        return self._map_response(raw_response)

    def _map_response(self, raw_response):

        return LLMResponse(
        answer=raw_response.message.content,
        model_name=raw_response.model,
        prompt_tokens=raw_response.prompt_eval_count,
        completion_tokens=raw_response.eval_count,
        response_time=raw_response.total_duration / 1000000000,
        finish_reason=raw_response.done_reason,
        created_at=raw_response.created_at,
    )
