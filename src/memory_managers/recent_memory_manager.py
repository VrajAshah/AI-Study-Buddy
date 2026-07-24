from src.memory_managers.base_memory_manager import BaseMemoryManager

class RecentMemoryManager(BaseMemoryManager):

    def __init__(self, max_messages=4):
        self.max_messages = max_messages

    def get_context(self, memory, current_question):

        history = memory.get_history()

        return history[-self.max_messages:]