import os  # ✅ Make sure this is at the top!
from flask import Flask, request, jsonify, render_template
from src.main import get_response

app = Flask(__name__)  # ✅ Note: double underscores, not _name_

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ This is needed for Render
    app.run(debug=True, host="0.0.0.0", port=port)

