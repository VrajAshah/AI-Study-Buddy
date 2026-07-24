from src.rerankers.BaseReranker import BaseReranker

class NoOpReranker(BaseReranker):

    def rerank(self,query, retrieval_results, top_k):

        return retrieval_results[:top_k]