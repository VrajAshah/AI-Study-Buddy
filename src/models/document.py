from src.models.document_type import DocumentType

class Document:

    def __init__(self,pages,name):
        self.name = name
        self.pages = pages
        self.document_type = DocumentType.UNKNOWN
        self.summary = None
        self.language = None
        self.chunks = []