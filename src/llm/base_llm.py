from abc import ABC,abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, prompt):
        print("generate -----BaseLLM----->>>")
        pass