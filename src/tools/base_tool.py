from abc import ABC, abstractmethod

class BaseTool(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass
