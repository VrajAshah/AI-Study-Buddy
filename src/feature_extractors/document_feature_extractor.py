from src.config.document_rules import DOCUMENT_RULES

class DocumentFeatureExtractor:

    def _get_document_text(self, document):
        texts = []

        for page in document.pages:
            texts.append(page.cleaned_text.lower())

        return " ".join(texts)
    
    def extract(self,document):
        features = {}

        features["page_count"] = len(document.pages)

        text = self._get_document_text(document)

        keywords = set()

        for rule in DOCUMENT_RULES.values():
            keywords.update(rule["keywords"].keys())

        for keyword in keywords:
            features[f"{keyword}_count"] = text.count(keyword)

        return features