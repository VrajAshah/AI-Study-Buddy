from dataclasses import dataclass

@dataclass
class RetrieverConfig:

    retriever = "mmr"
    top_k = 20
    rerank_top_k = 3