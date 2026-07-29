from abc import ABC, abstractmethod

class BaseDecisionEngine(ABC):

    @abstractmethod
    def decide(self, context):
        pass