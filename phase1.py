import requests
import json

# utilisation url 
symbole = 'goog'
url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

params = {
    'début': '2019-02-18',
    'fin': '2019-02-24',
}

réponse = requests.get(url=url, params=params)
réponse = json.loads(réponse.text)
print(réponse)