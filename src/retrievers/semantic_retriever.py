import math

class SemanticRetriever:

    def __init__(self,embedding_generator):
        self.embedding_generator = embedding_generator

    
    def retrieve(self,document,question):

        question_embedding = self.embedding_generator.generate_embedding(question)
        best_chunk = None
        best_score = -1

        for chunk in document.chunks:
            score = self._cosine_similarity(chunk.embedding,question_embedding)
            if score > best_score:
                best_score = score
                best_chunk = chunk
        return best_chunk

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