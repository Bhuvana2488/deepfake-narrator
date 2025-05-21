from flask import Flask, render_template, request, send_file, jsonify
import requests
import json
import os

app = Flask(__name__)  # Corrected initialization of Flask app

# Your ElevenLabs API Key
API_KEY = "sk_977116ea851ef52606945db7ed1fb09edb7dbc9720e1cbf5"

# Voice ID (Choose from ElevenLabs' default voices or your custom voice)
voice_id = "gIzHhB1fOOHrsUzJkMBM"  # Replace with your ElevenLabs voice ID

# Endpoint for ElevenLabs API
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html page when accessing the root URL

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text', '')  # Extract text from the request body

    # ElevenLabs API request headers
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    # Voice settings for human-like output
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.15,
            "similarity_boost": 0.98
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Save the audio to a file
        audio_file_path = "output.mp3"
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)
        
        # Send the audio file as a response
        return send_file(audio_file_path, mimetype="audio/mpeg", as_attachment=True, download_name="output.mp3")
    else:
        return jsonify({"error": "Failed to generate audio"}), response.status_code




@app.route('/generate-audio_1', methods=['POST'])
def generate_audio_1():
    data = request.json
    text = data.get('text', '')  # Extract text from the request body

    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.15,
            "similarity_boost": 0.98
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Save the audio to a file
        audio_file_path = "output.mp3"
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)
        
        # Send the audio file as a response
        return send_file(audio_file_path, mimetype="audio/mpeg", as_attachment=True, download_name="output.mp3")
    else:
        return jsonify({"error": "Failed to generate audio"}), response.status_code

if __name__ == '_main':  # Corrected __name check
    app.run(debug=True)