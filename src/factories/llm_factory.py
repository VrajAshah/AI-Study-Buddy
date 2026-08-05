from dotenv import load_dotenv
import os
from src.llm.gemini_llm import GeminiLLM
from src.llm.ollama_llm import Ollama
from src.config.settings import settings


class LLMFactory:

    @staticmethod
    def create():
        provider = settings.llm.provider

        if provider == "gemini":

            load_dotenv()

            return GeminiLLM(
                api_key=os.getenv("GEMINI_API_KEY")
            )

        elif provider == "ollama":

            return Ollama(
                model_name=settings.llm.model
            )

        raise ValueError(
            f"Unknown LLM provider: {provider}"
        )