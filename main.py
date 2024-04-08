#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq
import json

file = open('outfits.json')
outfitsData = json.load(file)

"""
sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme")
styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : été\n2 : automne\n3 : hiver\n 4 : printemps")
cityInput = input("Veuillez rentrer un nom de ville")
"""
langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"
apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={cityInput}&appid={apiKey}&lang={langue}"

def questionnaire():
    sexe = input("Êtes vous un homme ou une femme ?\n0 : femme\n1 : homme\n")
    styleVestimentaire = input("Veuillez faire votre choix vestimentaire :\n1 : été\n2 : automne\n3 : hiver\n 4 : printemps\n")
    cityInput = input("Veuillez rentrer un nom de ville\n")
    json = rq.get(apiLink).json()
    JSON = json['weather'][0]['description']
    return JSON

if (JSON.)


file.close()
print(JSON)

