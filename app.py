from PyPDF2 import PdfReader
from text_cleaner import clean_text

reader = PdfReader("03_invoice_sample.pdf")

print(len(reader.pages))

for page_numner, page in enumerate(reader.pages, start=1):
    print(page_numner)
    text = page.extract_text()
    print("text", text)
    cleaned = clean_text(text)
    print("cleaned", cleaned)
