from src.memory.base_memory import BaseMemory

class ConversationMemory(BaseMemory):

    def __init__(self):
        self.messages = []

    def add_message(self, role, message):
        self.messages.append(
            {
                "role": role,
                "message": message,
            }
        )

    def get_history(self):
        return self.messages

    def clear_history(self):
        self.messages.clear()