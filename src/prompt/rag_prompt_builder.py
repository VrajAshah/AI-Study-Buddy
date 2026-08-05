from .base_prompt_builder import BasePromptBuilder
from .prompt_context import PromptContext

from src.prompts.rag_prompt import RAG_PROMPT


class RAGPromptBuilder(BasePromptBuilder):

    def build(self,context: PromptContext):

        prompt_chunks = []

        for result in context.retrieval_results:

            chunk = result.chunk

            prompt_chunks.append(
                f"""
                    Document : {chunk.document_name}

                    Page : {chunk.page_number}

                    {chunk.text}
                """
                    )

        prompt_context = "\n\n-------------------------\n\n".join(prompt_chunks)

        prompt = RAG_PROMPT.format(
                    history=context.history,
                    context="\n\n".join(prompt_context),
                    question=context.question
                )

        return prompt