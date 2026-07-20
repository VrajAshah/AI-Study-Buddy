from src.indexing.document_indexing import DocumentIndexer
from src.retrievers.semantic_retriever import SemanticRetriever
from src.prompt.prompt_builder import PromptBuilder
from src.llm.base_llm import BaseLLM


class RAGPipeline:

    def __init__(
        self,
        indexer: DocumentIndexer,
        retriever: SemanticRetriever,
        prompt_builder: PromptBuilder,
        llm: BaseLLM
    ):
        self.indexer = indexer
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

        self.document = None

    def load_document(self, document):

        self.document = self.indexer.index(document)

    def ask(self, question):

        retrieval_results = self.retriever.retrieve(
            self.document,
            question
        )

        prompt = self.prompt_builder.build(
            question,
            retrieval_results
        )
        print("prompt ---------->>>", prompt)
        # prompt = """You are a helpful AI assistant.

        #             Context:
        #             Deep learning uses neural networks.

        #             Question:
        #             What does deep learning use?

        #             Answer in one complete sentence."""
        # print("prompt ---------->>>", prompt)

        response = self.llm.generate(prompt)
        print("response ---------->>>", response)

        return response