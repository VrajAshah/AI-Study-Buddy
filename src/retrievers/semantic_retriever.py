import math
from src.retrievers.base_retriever import BaseRetriever
from src.models.retrieval_result import RetrievalResult

class SemanticRetriever(BaseRetriever):

    def __init__(self,embedding_generator):
        self.embedding_generator = embedding_generator

    def retrieve(self,store,query, top_k):

        question_embedding = self.embedding_generator.generate_embedding(query)

        best_chunk_list = []

        for chunk in store.get_chunks():
            score = self._cosine_similarity(chunk.embedding,question_embedding)

            best_chunk_list.append(RetrievalResult(chunk,score))
            best_chunk_list = self._prepare_best_chunk_list(best_chunk_list,top_k)
        
        return best_chunk_list
    
    def _prepare_best_chunk_list(self, best_chunk_list,top_k):
        if len(best_chunk_list) > top_k:
            best_chunk_list.sort(reverse= True,key=lambda x: x.score)
            best_chunk_list.pop()

        return best_chunk_list
