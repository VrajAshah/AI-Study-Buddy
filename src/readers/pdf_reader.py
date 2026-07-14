from PyPDF2 import PdfReader

class PDFReader:

    def __init__(self,pdf_path: str):
        self.render = PdfReader(pdf_path)

    def get_pages(self):
        return self.render.pages
    
    def total_pages(self):
        return len(self.render.pages)