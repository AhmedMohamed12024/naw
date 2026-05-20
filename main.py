import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Reads the secure key variables out of the Render Environment dashboard settings
GEMINI_KEY = os.environ.get("GEMINI_KEY")
API_URL = f"https://googleapis.com{GEMINI_KEY}"

@app.route('/chat', methods=['POST'])
def cloud_chat():
    try:
        roblox_payload = request.get_json()
        response = requests.post(API_URL, json=roblox_payload, headers={"Content-Type": "application/json"})
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Render requires binding directly onto host 0.0.0.0 via port 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
