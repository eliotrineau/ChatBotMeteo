#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json as json_module
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/questionnaire": {"origins": "*"}})

def sexe():
    os.system('clear')
    sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme\n")
    return sexe

def styleVestimentaire():
    os.system('clear')
    styleVestimentaire = input("Veuillez faire votre choix de saison:\n1 : printemps\n2 : été\n3 : automne\n4 : hiver\n")
    return styleVestimentaire

def cityInput():
    os.system('clear')
    cityInput = input("Veuillez rentrer un nom de ville:\n")
    return cityInput


langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"

@app.route('/questionnaire', methods=['POST'])
def questionnaire():
    city = cityInput()
    apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={langue}"
    response = rq.get(apiLink)
    weather_data = response.json()
    weather = weather_data['weather'][0]['description']

    gender = sexe()
    style = styleVestimentaire()

    with open('outfits.json') as file:
        outfitsData = json_module.load(file)

    # Determine the outfit based on the weather
    if "rain" in weather:
        weather = "pluvieux"
    elif "cloud" in weather:
        weather = "nuageux"
    elif "snow" in weather:
        weather = "neige"
    elif "clear" in weather or "ciel dégagé" in weather:
        weather = "ensoleillé"

    if gender == "0":  # femme
        if style == "1":  # printemps
            return jsonify({"outfit1": outfitsData["femme"]["printemps"][weather], "outfit2": outfitsData["femme"]["printemps"][weather]})
        elif style == "2":  # été
            return jsonify({"outfit1": outfitsData["femme"]["été"][weather], "outfit2": outfitsData["femme"]["été"][weather]})
        elif style == "3":  # automne
            return jsonify({"outfit1": outfitsData["femme"]["automne"][weather], "outfit2": outfitsData["femme"]["automne"][weather]})
        elif style == "4":  # hiver
            return jsonify({"outfit1": outfitsData["femme"]["hiver"][weather], "outfit2": outfitsData["femme"]["hiver"][weather]})
        else:
            return "Choix vestimentaire invalide."

    elif gender == "1":  # homme
        if style == "1":  # printemps
            return jsonify({"outfit1": outfitsData["hommes"]["printemps"][weather], "outfit2": outfitsData["hommes"]["printemps"][weather]})
        elif style == "2":  # été
            return jsonify({"outfit1": outfitsData["hommes"]["été"][weather], "outfit2": outfitsData["hommes"]["été"][weather]})
        elif style == "3":  # automne
            return jsonify({"outfit1": outfitsData["hommes"]["automne"][weather], "outfit2": outfitsData["hommes"]["automne"][weather]})
        elif style == "4":  # hiver
            return jsonify({"outfit1": outfitsData["hommes"]["hiver"][weather], "outfit2": outfitsData["hommes"]["hiver"][weather]})
        else:
            return "Choix vestimentaire invalide."

    else:
        return "Sexe invalide."

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
