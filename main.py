#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json


"""
sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme")
styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : été\n2 : automne\n3 : hiver\n 4 : printemps")
cityInput = input("Veuillez rentrer un nom de ville")
"""
langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"
apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={cityInput}&appid={apiKey}&lang={langue}"

def sexe():
    sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme")
    return sexe

def styleVestimentaire():
    styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : été\n2 : automne\n3 : hiver\n 4 : printemps")
    return styleVestimentaire

def cityInput():
    cityInput = input("Veuillez rentrer un nom de ville")
    return cityInput

def questionnaire():
    sexe()
    styleVestimentaire()
    cityInput()
    json = rq.get(apiLink).json()
    JSON = json['weather'][0]['description']
    return JSON


def get_outfit(sexe, styleVestimentaire):
    file = open('outfits.json')
    outfitsData = json.load(file)
    file.close()

    if sexe == "1":  # femme
        if styleVestimentaire == "1":  # printemps
            return outfitsData["femme"]["printemps"]
        elif styleVestimentaire == "2":  # été
            return outfitsData["femme"]["été"]
        elif styleVestimentaire == "3":  # automne
            return outfitsData["femme"]["automne"]
        elif styleVestimentaire == "4":  # hiver
            return outfitsData["femme"]["hiver"]
        else:
            return "Choix vestimentaire invalide."

    elif sexe == "0":  # homme
        if styleVestimentaire == "1":  # été
            return outfitsData["homme"]["été"]
        elif styleVestimentaire == "2":  # automne
            return outfitsData["homme"]["automne"]
        elif styleVestimentaire == "3":  # hiver
            return outfitsData["homme"]["hiver"]
        elif styleVestimentaire == "4":  # printemps
            return outfitsData["homme"]["printemps"]
        else:
            return "Choix vestimentaire invalide."

    else:
        return "Sexe invalide."

# Example usage:
sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme\n")
styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : été\n2 : automne\n3 : hiver\n 4 : printemps\n")
outfit = get_outfit(sexe, styleVestimentaire)
print(outfit)

print(JSON)

