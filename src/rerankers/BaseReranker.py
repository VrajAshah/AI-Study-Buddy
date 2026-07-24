from abc import ABC,abstractmethod

class BaseReranker(ABC):

    @abstractmethod
    def rerank(self,query, retrieval_results, top_k):
        pass