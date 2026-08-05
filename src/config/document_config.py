from dataclasses import dataclass

@dataclass
class DocumentConfig:

    chunk_size = 600
    chunk_overlap = 100
    cleaner = "default"
    chunker = "sentence"
    store = "memory"