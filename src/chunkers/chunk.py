class Chunk:

    def __init__(self,chunk_id,page_number,text, document_name):
        self.chunk_id = chunk_id
        self.page_number = page_number
        self.text = text
        self.document_name = document_name
        self.embedding = None

    def __str__(self):
        return f"Chunk {self.chunk_id} (Page {self.page_number}) {self.text}"
    
    def __repr__(self):
        return self.__str__()