from src.config.settings import settings

from src.retrievers.mmr_retriever import MMRRetriever
from src.retrievers.semantic_retriever import SemanticRetriever


class RetrieverFactory:

    @staticmethod
    def create(generator):

        retriever = settings.retriever.retriever

        if retriever == "mmr":
            return MMRRetriever(generator)

        elif retriever == "semantic":
            return SemanticRetriever(generator)

        raise ValueError(
            f"Unknown retriever: {retriever}"
        )