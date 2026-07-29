from abc import ABC, abstractmethod

class BaseWorkflow(ABC):

    @abstractmethod
    def execute(self, context, decision):
        pass