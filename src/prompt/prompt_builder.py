from src.prompts.rag_prompt import RAG_PROMPT

class PromptBuilder:

    def build(self,question,retrieval_results):
        context = []
        for result in retrieval_results:
            context.append(result.chunk.text)

        context = "\n\n".join(context)
        
        prompt = RAG_PROMPT.format(context = context, question = question)

        return prompt
        