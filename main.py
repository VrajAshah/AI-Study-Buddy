from src.analyzers.document_analyzer import DocumentAnalyzer
from src.readers.pdf_reader import PDFReader
from src.cleaners.text_cleaner import TextCleaner
from src.models.document import Document
from src.chunkers.sentence_chunker import SentenceChunker
from src.classifiers.document_classifier import DocumentClassifier
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.retrievers.semantic_retriever import SemanticRetriever
from src.retrievers.mmr_retriever import MMRRetriever
from src.prompt.prompt_builder import PromptBuilder
from src.llm.ollama_llm import Ollama
from src.indexing.document_indexing import DocumentIndexer
from src.pipeline.rag_pipeline import RAGPipeline
from src.rerankers.NoOpReranker import NoOpReranker
from src.memory.conversation_memory import ConversationMemory
from src.memory_managers.recent_memory_manager import RecentMemoryManager

document_name = "01_article_text.pdf"
reader = PDFReader(document_name)
pages = reader.get_pages()

analyzer  = DocumentAnalyzer(pages)
analyzed_pages = analyzer.analyze()

document = Document(analyzed_pages,document_name)

generator = EmbeddingGenerator()
reranker = NoOpReranker()

indexer = DocumentIndexer(embedding_generator= generator,cleaner= TextCleaner(),chunker= SentenceChunker())
index_document = indexer.index(document)

semantic_pipeline = RAGPipeline(
    indexer=indexer,
    retriever=SemanticRetriever(generator),
    reranker=reranker,
    prompt_builder=PromptBuilder(),
    llm=Ollama("gemma3:1b"),
    memory=ConversationMemory(),
    memory_manager=RecentMemoryManager()
)

mmr_pipeline = RAGPipeline(
    indexer=indexer,
    retriever=MMRRetriever(generator),
    reranker=reranker,
    prompt_builder=PromptBuilder(),
    llm=Ollama("gemma3:1b"),
    memory=ConversationMemory(),
    memory_manager=RecentMemoryManager()
)

semantic_pipeline.load_document(document)

response = semantic_pipeline.ask(
    "What deep learning uses?"
)
print("semantic_pipeline",response.answer)

mmr_pipeline.load_document(document)

response = mmr_pipeline.ask(
    "What deep learning uses?"
)

print("mmr_pipeline",response.answer)

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
        response = semantic_pipeline.ask(question)
        print("semantic_pipeline: ",response.answer)
        response = mmr_pipeline.ask(question)
        print("mmr_pipeline: ",response.answer)

        # retrieve_best_chunk = retrieval.retrieve(document, question)
        # print("\n[Answer] ---------->>>", retrieve_best_chunk)
    except Exception as e:
        print(f"An error occurred while retrieving the answer: {e}")
