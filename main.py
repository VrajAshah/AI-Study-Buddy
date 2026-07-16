from src.analyzers.document_analyzer import DocumentAnalyzer
from src.readers.pdf_reader import PDFReader
from src.cleaners.text_cleaner import TextCleaner
from src.models.document import Document
from src.chunkers.sentence_chunker import SentenceChunker
from src.classifiers.document_classifier import DocumentClassifier
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.retrievers.semantic_retriever import SemanticRetriever

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

# print(document.chunks)

generator = EmbeddingGenerator()
document = generator.generate_document_embeddings(document)

question = "What deep learning uses?"
# question_embedding = generator.generate_embedding(question)
# print("question_embedding ---------->>>", len(question_embedding))

retrieval = SemanticRetriever(generator)
retrieve_best_chunk = retrieval.retrieve(document,question)
print("retrieve_best_chunk ---------->>>", retrieve_best_chunk)

print("\n--- Document processing complete. Ask your questions! (Type 'quit' or 'exit' to stop) ---")

# Start an interactive loop
while True:
    # 1. Prompt the user for input
    question = input("\nAsk a question: ").strip()
    
    # 2. Check for an exit command
    if question.lower() in ['quit', 'exit', 'q']:
        print("Exiting search. Goodbye!")
        break
        
    # 3. Skip empty inputs
    if not question:
        print("Please enter a valid question.")
        continue
        
    # 4. Retrieve and print the answer
    try:
        retrieve_best_chunk = retrieval.retrieve(document, question)
        print("\n[Answer] ---------->>>", retrieve_best_chunk)
    except Exception as e:
        print(f"An error occurred while retrieving the answer: {e}")
