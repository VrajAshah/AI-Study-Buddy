from src.config.document_rules import DOCUMENT_RULES
from src.models.document_type import DocumentType
from src.feature_extractors.document_feature_extractor import DocumentFeatureExtractor

class DocumentClassifier:

    def classify(self, document):

        document_extractor = DocumentFeatureExtractor()
        features = document_extractor.extract(document)
        print("features", features)

        scores = {}
        for document_name, rule in DOCUMENT_RULES.items():
            print("rule", rule)
            scores[document_name] = 0
            print("scores", scores)

            print("rule[keywords].items", rule["keywords"].items())
            for keyword, weight in rule["keywords"].items():
                scores[document_name] += features[f"{keyword}_count"] * weight
                # if keyword in text:
                #     scores[document_name] += weight

        print(scores)

        winner = max(scores,key=scores.get)

        if scores[winner] == 0:
            document.document_type = DocumentType.UNKNOWN
        else:
            document.document_type = DocumentType[winner]
        print("document.document_type", document.document_type)

        return document