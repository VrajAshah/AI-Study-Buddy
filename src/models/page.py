class Page:

    def __init__(self,number,page_type, raw_text = ""):
        self.number = number
        self.page_type = page_type
        self.raw_text = raw_text
        self.cleaned_text = None
        self.chunks = []
        self.embeddings = None
        self.language = None
        


    def __str__(self):
        # return f"Page {self.number} ({self.page_type.name}) {self.raw_text} {self.cleaned_text}"
        return f"Page {self.number} ({self.page_type.name}) {len(self.raw_text)} {len(self.cleaned_text)}"

    def __repr__(self):
        return self.__str__()