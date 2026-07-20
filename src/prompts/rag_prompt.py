RAG_PROMPT = """
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

If the answer cannot be found in the context,
say:
"I couldn't find the answer in the uploaded document."

-------------------------
Context:

{context}

-------------------------

Question:

{question}

Provide a concise answer using the above context only.

"""