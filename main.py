import requests
import json
from API import api


city = 'Bangkok'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

res = requests.get(url)


with open("weathe.txt", "w", encoding="UTF-8") as file:
    file.write(res.text)

with open("weathe.json", "w") as file:
    json.dump(res.json(), file, indent=4)
with open("weathe.json", "r") as gb:
    polnoygb = json.load(gb)

#print(type(polnoygb))
temp = polnoygb['main']['temp']
print(f"В {polnoygb['name']} {polnoygb['weather'][0]['main']}, температура {int(temp)} С, "
      f"как всегда полно трансвеститов их их юбки задираются под скоростью ветра "
      f"{polnoygb['wind']['speed']} и просто лучше этого не видеть")

