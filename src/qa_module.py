from sentence_transformers import SentenceTransformer, util

class QAModule:
    def __init__(self, document_text):
        self.text = document_text
        self.sentences = [s.strip() for s in self.text.split('.') if len(s.strip()) > 20]
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(self.sentences, convert_to_tensor=True)

    def answer(self, query):
        if "price" in query.lower() or "cost" in query.lower():
            return "Please contact us on WhatsApp for cost-related queries: +91XXXXXXXXXX"
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        best_idx = scores.argmax()
        return self.sentences[best_idx]
