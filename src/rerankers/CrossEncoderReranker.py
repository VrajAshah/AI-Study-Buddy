from sentence_transformers import CrossEncoder
from src.rerankers.BaseReranker import BaseReranker

class CrossEncoderReranker(BaseReranker):

    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank(self,query, retrieval_results, top_k):

        sentence_pairs = [ [query,i.chunk.text] for i in retrieval_results ]
        scores = self.model.predict(sentence_pairs)

        for result, score in zip(retrieval_results, scores):
            result.score = score

        retrieval_results.sort(key=lambda result: result.score,reverse=True)

        return retrieval_results[:top_k]