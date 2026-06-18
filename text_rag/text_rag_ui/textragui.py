import os
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

API_KEY = os.getenv("OPENROUTER_API_KEY", "YOUR_KEY_HERE")
LLM_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL   = "openai/gpt-oss-120b:free"

# ── Serve frontend files ──
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")

# ── LLM proxy (no key in browser) ──
@app.route("/api/ask", methods=["POST"])
def ask():

    data = request.get_json()

    res = requests.post(
        LLM_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": data["prompt"]
                }
            ]
        },
    )

    print("STATUS:", res.status_code)
    print("RESPONSE:", res.text)
    
    if res.status_code != 200:
        return jsonify({
            "answer": f"OpenRouter Error: {res.text}"
        })

    reply = res.json()

    return jsonify({
        "answer": reply["choices"][0]["message"]["content"]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)