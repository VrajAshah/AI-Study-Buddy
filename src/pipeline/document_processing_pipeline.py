from src.readers.pdf_reader import PDFReader
from src.models.document import Document
from src.analyzers.document_analyzer import DocumentAnalyzer

from src.logging.logging import get_logger

logger = get_logger(__name__)

class DocumentProcessingPipeline:

    def __init__(self, indexer, store, state):
        self.indexer = indexer
        self.store = store 
        self.state = state

    def process(self, document_name):

        try:

            logger.info("Indexing started")
            reader = PDFReader(document_name)
            pages = reader.get_pages()

            analyzer = DocumentAnalyzer(pages)
            analyzed_pages = analyzer.analyze()

            document = Document(analyzed_pages, document_name)

            indexed_document = self.indexer.index(document)
            logger.info("Indexing Completed")

            self.store.add_document(indexed_document)

            self.state.add_document(document_name)

            return indexed_document
        
        except Exception as e:
            logger.error("Error in indexing document " + str(e))
            logger.exception(e)