from abc import ABC, abstractmethod

class BasePipeline(ABC):

    @abstractmethod
    def ask(self, question, tool_name):
        pass