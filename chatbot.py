from flask import Blueprint, request, jsonify
from openai import OpenAI

chatbot_bp = Blueprint('chatbot', __name__)
client = OpenAI(api_key="your_openai_api_key_here")

# ===== Load knowledge base =====
def load_knowledge():
    with open("knowledge.txt", "r", encoding="utf-8") as f:
        return f.read().split("\n")

knowledge_base = load_knowledge()


# ===== Simple retrieval (keyword match) =====
def retrieve_context(query):
    relevant_chunks = []

    for line in knowledge_base:
        if any(word.lower() in line.lower() for word in query.split()):
            relevant_chunks.append(line)

    return " ".join(relevant_chunks[:3])  # limit context


# ===== Chat route =====
@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")

    try:
        # 🔹 Retrieve relevant context
        context = retrieve_context(user_input)

        # 🔹 Augment prompt
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": user_input}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content

        return jsonify({
            "response": reply,
            "context_used": context  # optional (good for debugging)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
