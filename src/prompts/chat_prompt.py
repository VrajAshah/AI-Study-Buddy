CHAT_PROMPT = """
You are a helpful AI assistant.

Maintain a natural and coherent conversation.

Use the previous conversation history when it is relevant.

If the question is unrelated to the history,
answer it independently.

-------------------------
Conversation History:

{history}

-------------------------

Question:

{question}

Provide a clear, concise, and helpful response.
"""