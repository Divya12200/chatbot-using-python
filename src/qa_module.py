from sentence_transformers import SentenceTransformer, util

class QAModule:
    def __init__(self, chunks):
        self.chunks = chunks
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(chunks, convert_to_tensor=True)

    def answer(self, query):
        query_lower = query.lower()

        # 🎉 Greet users
        greetings = ["hi", "hello", "hey", "good morning", "good evening"]
        if any(greet in query_lower for greet in greetings):
            return "👋 Welcome to Huezone Solutions!\nHow can I assist you today?"

        # 💰 Handle pricing/cost questions
        if "price" in query_lower or "cost" in query_lower:
            return (
                "💬 For cost-related queries, please contact us on WhatsApp: +91 9108684414"
                "<br><br>🔗 <a href='https://www.indiamart.com/huezone-solutions/' target='_blank'>Visit us here</a>")

        # 🔍 Semantic search on PDF content
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        best_idx = scores.argmax().item()
        best_score = scores[best_idx].item()

        # ❓ Low confidence fallback
        if best_score < 0.4:
            return (
                "❓ Sorry, I couldn't find anything relevant. Can you rephrase your question?"
                "<br><br>🔗 <a href='https://www.indiamart.com/huezone-solutions/' target='_blank'>Visit us here</a>")

        return (
            f"{self.chunks[best_idx]}"
            "<br><br>🔗 <a href='https://www.indiamart.com/huezone-solutions/' target='_blank'>Visit us here</a>")
