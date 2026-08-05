from src.memory.conversation_memory import ConversationMemory
from src.memory_managers.recent_memory_manager import RecentMemoryManager
from src.config.settings import settings

class MemoryFactory:

    @staticmethod
    def create_memory():

        return ConversationMemory()

    @staticmethod
    def create_manager():

        manager = settings.memory.manager

        if manager == "recent":
            return RecentMemoryManager()

        raise ValueError(
            f"Unknown memory manager: {manager}"
        )