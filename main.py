#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json as json_module
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"

@app.route('/questionnaire', methods=['POST'])
def questionnaire():
    data = request.get_json()
    city = data.get('cityInput')
    sexe = data.get('sexeInput')
    saison = data.get('saisonInput')
    if not city or not isinstance(city, str):
        return jsonify({"error": "Invalid city name."}), 400
    apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={langue}"
    response = rq.get(apiLink)
    weather_data = response.json()
    if weather_data.get('cod') == '404':
        return jsonify({"error": "City not found."}), 404

    weather = weather_data['weather'][0]['description']

    gender = sexe
    style = saison

    with open('C:/Users/Anton/tes/FINALB2/outfits.json') as file:
        outfitsData = json_module.load(file)

    # Determine the outfit based on the weather
    if "rain" in weather:
        weather = "pluvieux"
    elif "cloud" in weather or "peu nuageux" in weather:
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
 
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)
