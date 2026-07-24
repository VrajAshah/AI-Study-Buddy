from src.store.base_store import BaseStore

class InMemoryDocumentStore(BaseStore):

    def __init__(self):
        self._chunks = []

    def add_document(self,document):
        self._chunks.extend(document.chunks)

    def get_chunks(self):
        return self._chunks

    def clear(self):
        self._chunks.clear()