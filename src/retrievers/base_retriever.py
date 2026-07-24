import math
from abc import ABC,abstractmethod

class BaseRetriever(ABC):

    @abstractmethod
    def retrieve(self, store, query, top_k=3):
        pass 

    def _dot_product(self, vector1, vector2):

        dot_product = sum(x * y for x, y in zip(vector1, vector2))
        return dot_product

    def _vector_length(self, vector):

        length = math.sqrt(sum(x ** 2 for x in vector))
        return length
    
    def _cosine_similarity(self, vector1, vector2):

        dot_product = self._dot_product(vector1, vector2)
        len_vector1 = self._vector_length(vector1)
        len_vector2 = self._vector_length(vector2)

        if len_vector1 == 0 or len_vector2 == 0:
            return 0
        
        return dot_product / (len_vector1 * len_vector2)