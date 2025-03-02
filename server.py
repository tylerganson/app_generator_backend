import openai
import os
from flask import Flask, request, jsonify

# ✅ Load API Key from Environment Variables (Google Cloud Compatible)
API_KEY = os.getenv("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")
if not API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in Google Cloud Environment Variables.")

openai.api_key = API_KEY

# ✅ Initialize Flask App
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Create a full Flutter app: {prompt}"}]
        )
        
        return jsonify({"code": response['choices'][0]['message']['content']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))


