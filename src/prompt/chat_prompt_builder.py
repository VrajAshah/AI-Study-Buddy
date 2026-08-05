from src.prompts.chat_prompt import CHAT_PROMPT
from .base_prompt_builder import BasePromptBuilder


class ChatPromptBuilder(BasePromptBuilder):

    def build(self,context):

        return CHAT_PROMPT.format(
            history=context.history,
            question=context.question
        )