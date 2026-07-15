from src.analyzers.document_analyzer import DocumentAnalyzer
from src.readers.pdf_reader import PDFReader
from src.cleaners.text_cleaner import TextCleaner
from src.models.document import Document
from src.chunkers.sentence_chunker import SentenceChunker
from src.classifiers.document_classifier import DocumentClassifier
from src.embeddings.embedding_generator import EmbeddingGenerator

reader = PDFReader("01_article_text.pdf")
pages = reader.get_pages()

analyzer  = DocumentAnalyzer(pages)
analyzed_pages = analyzer.analyze()

document = Document(analyzed_pages)

# for page in document.pages:
#     print("page", page.raw_text)

cleaner = TextCleaner()
document = cleaner.clean(document)

classifier = DocumentClassifier()
document = classifier.classify(document)

chunker =  SentenceChunker()
document = chunker.chunk(document)

print(document.chunks)

generator = EmbeddingGenerator()
document = generator.generate(document)

for chunk in document.chunks:
    print("chunk ---------->>>")
    print(chunk.text)
    print("embedding -------->>")
    print(type(chunk.embedding))
    print(len(chunk.embedding))
    print(chunk.embedding[:10])
