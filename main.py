#b09e3c93acf17d44ab9a805b88b2a074 //API KEY


import requests as rq

cityInput = input("Veuillez rentrer un nom de ville")
langue = "fr"
apiKey = "b09e3c93acf17d44ab9a805b88b2a074"
apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={cityInput}&appid={apiKey}&lang={langue}"


json = rq.get(apiLink).json
JSON = json['weather'][0]['description']

print(JSON)