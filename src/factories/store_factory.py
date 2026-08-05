from src.config.settings import settings
from src.store.in_memory_store import InMemoryDocumentStore

class StoreFactory:

    @staticmethod
    def create():

        provider = settings.document.store

        if provider == "memory":
            return InMemoryDocumentStore()

        raise ValueError(
            f"Unknown document store: {provider}"
        )