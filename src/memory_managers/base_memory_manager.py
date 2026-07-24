from abc import ABC,abstractmethod

class BaseMemoryManager(ABC):

    @abstractmethod
    def get_context(self, memory, current_question):
        pass