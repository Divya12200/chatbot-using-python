from sentence_transformers import SentenceTransformer, util

class QAModule:
    def __init__(self, chunks):
        self.chunks = chunks
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(chunks, convert_to_tensor=True)

    def answer(self, query):
        query_lower = query.lower()

        # 🎉 Greeting
        if any(greet in query_lower for greet in ["hi", "hello", "hey", "good morning", "good evening"]):
            return "👋 Welcome to Huezone Solutions! How can I assist you today?", 1.0

        # 💰 Price/cost-related questions
        if "price" in query_lower or "cost" in query_lower:
            return (
                "🛒 Buy via IndiaMART or contact us on WhatsApp: +91 9108684414"
                "<br><br>🔗 <a href='https://www.indiamart.com/huezone-solutions/' target='_blank'>Buy via IndiaMART</a>"
            , 1.0)

        # 🔍 Try matching from PDF
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        best_idx = scores.argmax().item()
        best_score = scores[best_idx].item()

        if best_score >= 0.4:
            return self.chunks[best_idx], best_score

        # ❌ Not found in PDF
        return (
            "ℹ️ Please visit us via IndiaMART for more information."
            "<br><br>🔗 <a href='https://www.indiamart.com/huezone-solutions/' target='_blank'>Visit us via IndiaMART</a>"
        , best_score)
