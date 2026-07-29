from abc import ABC, abstractmethod

class BaseAgent(ABC):

    @abstractmethod
    def run(self, user_input: str):
        pass