class LLMResponse:

    def __init__(
        self,
        answer: str,
        model_name: str,
        prompt_tokens: int,
        completion_tokens: int,
        response_time: float,
        finish_reason: str,
        created_at: str | None = None
    ):
        self.answer = answer
        self.model_name = model_name
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.response_time = response_time
        self.finish_reason = finish_reason
        self.created_at = created_at

    @property
    def total_tokens(self):
        return self.prompt_tokens + self.completion_tokens

    def __str__(self):
        return self.answer

    def __repr__(self):
        return self.__str__()