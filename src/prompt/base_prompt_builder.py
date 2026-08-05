from abc import ABC, abstractmethod
from .prompt_context import PromptContext


class BasePromptBuilder(ABC):

    @abstractmethod
    def build(self,context: PromptContext) -> str:
        pass