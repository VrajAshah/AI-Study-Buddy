from abc import ABC,abstractmethod

class BaseMemory(ABC):

    @abstractmethod
    def add_message(self, role, message):
        pass

    @abstractmethod
    def get_history(self):
        pass

    @abstractmethod
    def clear_history(self):
        pass