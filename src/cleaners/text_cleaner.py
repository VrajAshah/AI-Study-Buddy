import re

class TextCleaner:

    # def __init__(self, page):
    #     self.page = page

    def clean(self,document):
        for page in document.pages:
            text = page.raw_text

            if text is None:
                page.cleaned_text = ""
                continue
            
            text = re.sub(r"\s+", " ", text)
            text = text.strip()

            page.cleaned_text = text

        return document