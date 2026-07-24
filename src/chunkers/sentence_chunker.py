import re

from src.chunkers.base_chunker import BaseChunker
from src.chunkers.chunk import Chunk

class SentenceChunker(BaseChunker):

    def chunk(self, document):
        chunk_id = 1

        for page in document.pages:

            sentences = re.split(r'(?<=[.!?])\s+', page.cleaned_text)

            for sentence in sentences:
                sentence = sentence.strip()
                if sentence:
                    chunk = Chunk(
                            chunk_id = chunk_id,
                            page_number = page.number,
                            text = sentence,
                            document_name = document.name
                        )
                    page.chunks.append(chunk)
                    document.chunks.append(chunk)
                        
                    chunk_id += 1

        return document