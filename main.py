#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json as json_module

def sexe():
    sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme\n")
    return sexe

def styleVestimentaire():
    styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : printemps\n2 : été\n3 : automne\n4 : hiver\n")
    return styleVestimentaire

def cityInput():
    cityInput = input("Veuillez rentrer un nom de ville\n")
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

    if gender == "0":  # femme
        if style == "1":  # printemps
            return outfitsData["femmes"]["printemps"][weather]
        elif style == "2":  # été
            return outfitsData["femmes"]["été"][weather]
        elif style == "3":  # automne
            return outfitsData["femmes"]["automne"][weather]
        elif style == "4":  # hiver
            return outfitsData["femmes"]["hiver"][weather]
        else:
            return "Choix vestimentaire invalide."

    elif gender == "1":  # homme
        if style == "1":  # été
            return outfitsData["hommes"]["été"][weather]
        elif style == "2":  # automne
            return outfitsData["hommes"]["automne"][weather]
        elif style == "3":  # hiver
            return outfitsData["hommes"]["hiver"][weather]
        elif style == "4":  # printemps
            return outfitsData["hommes"]["printemps"][weather]
        else:
            return "Choix vestimentaire invalide."

    else:
        return "Sexe invalide."


outfit = questionnaire()
print(outfit)
