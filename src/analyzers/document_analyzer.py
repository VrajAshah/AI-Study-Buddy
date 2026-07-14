from PyPDF2 import PdfReader
from src.models.page_type import PageType
from src.models.page import Page

class DocumentAnalyzer:

    def __init__(self,pages):
        self.pages = pages

    def analyze(self):
        results = []

        for page_number, pdf_page in enumerate(self.pages, start = 1):

            text = pdf_page.extract_text()

            if text and text.strip():
                page_type = PageType.TEXT
            else:
                page_type = PageType.IMAGE

            print("text", text)
            page = Page(number=page_number,page_type=page_type,raw_text = text if text else "")

            results.append(page)
        
        return results