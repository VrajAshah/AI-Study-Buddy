import math
from src.retrievers.base_retriever import BaseRetriever
from src.models.retrieval_result import RetrievalResult


class MMRRetriever(BaseRetriever):

    def __init__(self,embedding_generator):
        self.embedding_generator = embedding_generator

        self.lambda_multiplier = 0.7

    def retrieve(self,store,query, top_k):

        question_embedding = self.embedding_generator.generate_embedding(query)

        best_chunk_list = []

        for chunk in store.get_chunks():
            score = self._cosine_similarity(chunk.embedding,question_embedding)

            best_chunk_list.append(RetrievalResult(chunk,score))
            # best_chunk_list = self._prepare_mmr_chunk_list(best_chunk_list,top_k)
        
        return self._prepare_mmr_chunk_list(best_chunk_list, top_k)
    
    def _prepare_mmr_chunk_list(self,best_chunk_list,top_k):

        if not best_chunk_list:
            return []

        selected_chunks = []
        
        remaining_chunks = sorted(best_chunk_list,reverse=True,key=lambda x: x.score)[:10]
        selected_chunks.append(remaining_chunks.pop(0))


        while len(selected_chunks) <= top_k and remaining_chunks:
            best_candidate = None
            best_mmr_score = float("-inf")

            for chunk in remaining_chunks:
                relevance = chunk.score

                redundancy = self._max_similarity_to_selected(chunk,selected_chunks)

                mmr_score = (
                    self.lambda_multiplier * relevance
                    -
                    (1 - self.lambda_multiplier) * redundancy
                )

                if mmr_score > best_mmr_score:
                    best_mmr_score = mmr_score
                    best_candidate = chunk

            selected_chunks.append(best_candidate)
            remaining_chunks.remove(best_candidate)

        return selected_chunks

    def _max_similarity_to_selected(self,candidate,selected):
        
        max_similarity = 0

        for selected_chunk in selected:

            similarity = self._cosine_similarity(
                candidate.chunk.embedding,
                selected_chunk.chunk.embedding
            )

            max_similarity = max(
                max_similarity,
                similarity
            )

        return max_similarity

