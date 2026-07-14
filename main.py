from src.analyzers.document_analyzer import DocumentAnalyzer
from src.readers.pdf_reader import PDFReader
from src.cleaners.text_cleaner import TextCleaner
from src.models.document import Document
from src.chunkers.sentence_chunker import SentenceChunker

reader = PDFReader("01_article_text.pdf")

pages = reader.get_pages()

analyzer  = DocumentAnalyzer(pages)

analyzed_pages = analyzer.analyze()

document = Document(analyzed_pages)

for page in document.pages:
    print("page", page.raw_text)

cleaner = TextCleaner()
document = cleaner.clean(document)

chunker =  SentenceChunker()
document = chunker.chunk(document)

for page in document.pages:
    print("page")

    print(f"Page {page.number}")

    for chunk in page.chunks:

        print(chunk)

        print(chunk.text)
