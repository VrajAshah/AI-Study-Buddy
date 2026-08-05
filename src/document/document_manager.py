class DocumentManager:

    def __init__(self, pipeline, state):

        self.processing_pipeline = pipeline
        self.state = state

    def process_document(self, document_name):

        return self.processing_pipeline.process(document_name)

    def list_documents(self):

        return self.state.active_documents

    def has_documents(self):

        return len(self.state.active_documents) > 0

    def document_count(self):

        return len(self.state.active_documents)

    def clear_documents(self):

        self.state.clear_documents()

    def remove_document(self, document_name):

        self.state.remove_document(document_name)