from src.readers.pdf_reader import PDFReader
from src.models.document import Document
from src.analyzers.document_analyzer import DocumentAnalyzer

class DocumentProcessingPipeline:

    def __init__(self, indexer, store, state):
        self.indexer = indexer
        self.store = store 
        self.state = state

    def process(self, document_name):

        reader = PDFReader(document_name)
        pages = reader.get_pages()

        analyzer = DocumentAnalyzer(pages)
        analyzed_pages = analyzer.analyze()

        document = Document(analyzed_pages, document_name)

        indexed_document = self.indexer.index(document)

        self.store.add_document(indexed_document)

        self.state.add_document(document_name)

        return indexed_document