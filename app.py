from flask import Flask, render_template, request, send_file, jsonify
import requests
import json
import os

# Import chatbot blueprint
from chatbot import chatbot_bp

app = Flask(__name__)

# Register chatbot routes
app.register_blueprint(chatbot_bp)

# ===== ElevenLabs Config =====
API_KEY = "your_elevenlabs_api_key_here"
VOICE_ID = "gIzHhB1fOOHrsUzJkMBM"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"


# ===== Routes =====

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    payload = {
        "text": text[:2000],  # limit size (important)
        "voice_settings": {
            "stability": 0.15,
            "similarity_boost": 0.98
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            audio_file_path = "output.mp3"

            with open(audio_file_path, "wb") as audio_file:
                audio_file.write(response.content)

            return send_file(
                audio_file_path,
                mimetype="audio/mpeg",
                as_attachment=True,
                download_name="output.mp3"
            )
        else:
            return jsonify({"error": "TTS generation failed"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===== Run App =====
if __name__ == '__main__':
    app.run(debug=True)
