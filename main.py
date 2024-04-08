#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json as json_module

def sexe():
    sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme")
    return sexe

def styleVestimentaire():
    styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : été\n2 : automne\n3 : hiver\n 4 : printemps")
    return styleVestimentaire

def cityInput():
    cityInput = input("Veuillez rentrer un nom de ville")
    return cityInput


langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"


def questionnaire():
    # Set the different data
    city = cityInput()
    # Get the weather based on the location
    apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={langue}"
    response = rq.get(apiLink)
    weather_data = response.json()
    weather = weather_data['weather'][0]['description']

    gender = sexe()
    style = styleVestimentaire()

    with open('outfits.json') as file:
        outfitsData = json_module.load(file)
    file.close()

    # Determine the outfit based on the weather
    if "rain" in weather:
        weather = "pluvieux"
    elif "cloud" in weather:
        weather = "nuageux"
    elif "snow" in weather:
        weather = "neige"
    elif "clear" in weather:
        weather = "ensoleillé"

    if gender == "1":  # femme
        if style == "1":  # printemps
            return outfitsData["femme"]["printemps"][weather]
        elif style == "2":  # été
            return outfitsData["femme"]["été"][weather]
        elif style == "3":  # automne
            return outfitsData["femme"]["automne"][weather]
        elif style == "4":  # hiver
            return outfitsData["femme"]["hiver"][weather]
        else:
            return "Choix vestimentaire invalide."

    elif gender == "0":  # homme
        if style == "1":  # été
            return outfitsData["homme"]["été"][weather]
        elif style == "2":  # automne
            return outfitsData["homme"]["automne"][weather]
        elif style == "3":  # hiver
            return outfitsData["homme"]["hiver"][weather]
        elif style == "4":  # printemps
            return outfitsData["homme"]["printemps"][weather]
        else:
            return "Choix vestimentaire invalide."

    else:
        return "Sexe invalide."


outfit = questionnaire()
print(outfit)
