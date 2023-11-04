import requests
import json
import argparse


parser = argparse.ArgumentParser(description='On récupère les arguments')
parser.add_argument('entreprise', type=str, help='nom de entreprise')
parser.add_argument('date_debut', type=str, help='date debut')
parser.add_argument('date_fin', type=str, help='date de fin')
args = parser.parse_args()

# utilisation url 
symbole =args.entreprise
url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

params = {
    'début': args.date_debut,
    'fin': args.date_fin,
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