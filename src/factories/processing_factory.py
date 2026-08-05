from src.config.settings import settings
from src.cleaners.text_cleaner import TextCleaner
from src.chunkers.sentence_chunker import SentenceChunker
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.indexing.document_indexing import DocumentIndexer
from src.prompt.base_prompt_builder import BasePromptBuilder
from src.rerankers.NoOpReranker import NoOpReranker


class ProcessingFactory:

    @staticmethod
    def create_embedding_generator():

        return EmbeddingGenerator()

    @staticmethod
    def create_cleaner():

        if settings.document.cleaner == "default":
            return TextCleaner()

        raise ValueError(
            f"Unknown cleaner: {settings.document.cleaner}"
        )

    @staticmethod
    def create_chunker():

        if settings.document.chunker == "sentence":
            return SentenceChunker()

        raise ValueError(
            f"Unknown chunker: {settings.document.chunker}"
        )

    # @staticmethod
    # def create_prompt_builder():

    #     return BasePromptBuilder()

    @staticmethod
    def create_reranker():

        return NoOpReranker()

    @staticmethod
    def create_indexer(embedding_generator):

        cleaner = ProcessingFactory.create_cleaner()

        chunker = ProcessingFactory.create_chunker()

        return DocumentIndexer(
            embedding_generator=embedding_generator,
            cleaner=cleaner,
            chunker=chunker,
        )