from abc import ABC, abstractmethod

class BaseChunker(ABC):

    @abstractmethod
    def chunk(self, document):
        pass