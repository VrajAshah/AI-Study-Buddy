from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate_document_embeddings(self, document):

        for chunk in document.chunks:
            embedding = self.model.encode(chunk.text)
            chunk.embedding = embedding

        return document
    
    def generate_embedding(self, text):

        embedding = self.model.encode(text)
        return embedding