class RetrievalResult:

    def __init__(self,chunk,score):
        self.chunk = chunk
        self.score = score

    def __str__(self):
        return f"Result {self.score} {self.chunk}"
    
    def __repr__(self):
        return self.__str__()
