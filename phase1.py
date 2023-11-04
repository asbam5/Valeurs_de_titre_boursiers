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
réponse
## si reponse est bonne alors status_code=200
if réponse.status_code==200:
    réponse = json.loads(réponse.text)
    #for clé in réponse.keys():
    #    print(clé)
    print(réponse['historique']['2019-02-22'])
else:
    pass
    #print("error server avec un status %d et erreur %s",réponse.status_code,réponse.text)