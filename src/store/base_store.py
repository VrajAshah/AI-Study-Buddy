from abc import ABC,abstractmethod

class BaseStore(ABC):

    @abstractmethod
    def add_document(self, document):
        pass

    @abstractmethod
    def get_chunks(self):
        pass

    @abstractmethod
    def clear(self):
        pass