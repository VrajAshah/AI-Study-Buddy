from src.analyzers.document_analyzer import DocumentAnalyzer
from src.readers.pdf_reader import PDFReader
from src.cleaners.text_cleaner import TextCleaner
from src.models.document import Document
from src.chunkers.sentence_chunker import SentenceChunker
from src.classifiers.document_classifier import DocumentClassifier
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.retrievers.semantic_retriever import SemanticRetriever
from src.prompt.prompt_builder import PromptBuilder
from src.llm.ollama_llm import Ollama
from src.indexing.document_indexing import DocumentIndexer
from src.pipeline.rag_pipeline import RAGPipeline

reader = PDFReader("01_article_text.pdf")
pages = reader.get_pages()

analyzer  = DocumentAnalyzer(pages)
analyzed_pages = analyzer.analyze()

document = Document(analyzed_pages)

generator = EmbeddingGenerator()

indexer = DocumentIndexer(embedding_generator= generator,cleaner= TextCleaner(),chunker= SentenceChunker())
index_document = indexer.index(document)

pipeline = RAGPipeline(
    indexer=indexer,
    retriever=SemanticRetriever(generator),
    prompt_builder=PromptBuilder(),
    llm=Ollama("gemma3:1b")
)

pipeline.load_document(document)

response = pipeline.ask(
    "What deep learning uses?"
)

print(response.answer)

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
        response = pipeline.ask(question)

        print(response.answer)
        # retrieve_best_chunk = retrieval.retrieve(document, question)
        # print("\n[Answer] ---------->>>", retrieve_best_chunk)
    except Exception as e:
        print(f"An error occurred while retrieving the answer: {e}")
