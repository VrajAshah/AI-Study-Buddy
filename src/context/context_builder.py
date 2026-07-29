from src.context.context import Context

class ContextBuilder:

    def build(self, question, state):

        context =  Context(
            has_active_document= len(state.active_documents) > 0,
            has_history= len(state.conversation_history) > 0,
            tools_available= state.available_tools,
            question= question
        )

        return context