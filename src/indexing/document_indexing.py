from src.cleaners.text_cleaner import TextCleaner
from src.chunkers.sentence_chunker import SentenceChunker
# from src.embeddings.embedding_generator import EmbeddingGenerator


class DocumentIndexer:

    def __init__(
        self,
        embedding_generator,
        cleaner: TextCleaner,
        chunker: SentenceChunker
    ):
        self.cleaner = cleaner
        self.chunker = chunker
        self.embedding_generator = embedding_generator

    def index(self, document):
        self.cleaner.clean(document)
        self.chunker.chunk(document)
        self.embedding_generator.generate_document_embeddings(document)

        return document