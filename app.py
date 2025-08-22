from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load knowledge base
with open("data.json") as f:
    knowledge_base = json.load(f)

def find_answer(user_input):
    user_input_lower = user_input.lower()
    for item in knowledge_base:
        for keyword in item["keywords"]:
            if keyword.lower() in user_input_lower:
                return item["answer"]
    return "Sorry, I don't know the answer to that yet."

@app.route("/")
def index():
    return render_template("index.html")  # Your frontend file (e.g. chat.html)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = find_answer(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
