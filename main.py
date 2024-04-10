#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json as json_module
from werkzeug.utils import secure_filename
import os
import traceback
import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"

@app.route('/questionnaire', methods=['POST'])
def questionnaire():
    data = request.get_json()
    jour = int(data.get('jourInput'))    
    city = data.get('cityInput')
    sexe = data.get('sexeInput')
    saison = data.get('saisonInput')
    if not jour or not isinstance(jour, int):
        return jsonify({"error": "Invalid day."}, jour, {"type": isinstance(jour, int)}), 400
    if not city or not isinstance(city, str):
        return jsonify({"error": "Invalid city name."}), 400

    # Use the forecast API endpoint
    apiLink = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&lang={langue}"
    response = rq.get(apiLink)
    weather_data = response.json()
    if weather_data.get('cod') == '404':
        return jsonify({"error": "City not found."}), 404

    gender = sexe
    style = saison

    with open('C:/Users/Anton/tes/FINALB2/outfits.json') as file:
        outfitsData = json_module.load(file)

    # Default value for weather
    weather = "unknown"

    # Get the weather from the API response
    if jour == 0:
        weather = weather_data['list'][0]['weather'][0]['description']
    elif jour == 1:
        weather = weather_data['list'][8]['weather'][0]['description']

    # Determine the outfit based on the weather
    if "rain" in weather or "pluie modérée" in weather or "forte pluie" in weather or "légère pluie" in weather:
        weather = "pluvieux"
    elif "cloud" in weather or "peu nuageux" in weather or "couvert" in weather or "partiellement nuageux" in weather:
        weather = "nuageux"
    elif "snow" in weather:
        weather = "neige"
    elif "clear" in weather or "ciel dégagé" in weather:
        weather = "ensoleille"


    if gender == "0":  # femme
        if style == "1":  # printemps
            return jsonify({"outfit": outfitsData["femmes"]["printemps"][weather]})
        elif style == "2":  # été
            return jsonify({"outfit": outfitsData["femmes"]["ete"][weather]})
        elif style == "3":  # automne
            return jsonify({"outfit": outfitsData["femmes"]["automne"][weather]})
        elif style == "4":  # hiver
            return jsonify({"outfit": outfitsData["femmes"]["hiver"][weather]})
        else:
            return jsonify({"error": "Choix vestimentaire invalide."})

    elif gender == "1":  # homme
        if style == "1":  # printemps
            return jsonify({"outfit": outfitsData["hommes"]["printemps"][weather]})
        elif style == "2":  # été
            return jsonify({"outfit": outfitsData["hommes"]["ete"][weather]})
        elif style == "3":  # automne
            return jsonify({"outfit": outfitsData["hommes"]["automne"][weather]})
        elif style == "4":  # hiver
            return jsonify({"outfit": outfitsData["hommes"]["hiver"][weather]})
        else:
            return jsonify({"error": "Choix vestimentaire invalide."})

    else:
        return jsonify({"error": "Sexe invalide.", "gender": gender, "sexe": sexe, "data": data.get('sexe')}), 400

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get('city')

    if not city:
        return jsonify({"error": "City is required."}), 400

    response = rq.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={langue}')

    if response.status_code != 200: 
        return jsonify({"error": "Could not get weather."}), 500
    
    weather_data = response.json()

    weather = weather_data['weather'][0]['description']

    return jsonify({"weather": weather})

audio_files_dir = "C:\\Users\\Anton\\tes\\audio_files"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    print("Transcribing...")
    print(audio_files_dir)
    try:
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file"}), 400

        file = request.files['audio']
        filename = secure_filename(file.filename)
        if not filename.endswith('.ogg'):
            return jsonify({"error": "Invalid file format"}), 400

        filepath = os.path.join(audio_files_dir, filename)
        file.save(filepath)

        # Convert the .ogg file to .wav using pydub
        audio = AudioSegment.from_file(filepath, codec="opus")
        wav_filepath = filepath.replace('.ogg', '.wav')
        audio.export(wav_filepath, format="wav")

        if os.path.getsize(filepath) == 0:
            return jsonify({"error": "The file is empty"}), 400

        print(f"Saved .ogg file to {filepath}")

        if not os.path.exists(wav_filepath):
            return jsonify({"error": "Failed to convert .ogg file to .wav"}), 500

        print(f"Converted .ogg file to .wav at {wav_filepath}")

        # Transcribe the .wav file
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filepath) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="fr-FR")

        return jsonify({"message": "File uploaded, converted, and transcribed successfully", "transcription": text})
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        return jsonify({"error": str(e)}), 500
 
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)