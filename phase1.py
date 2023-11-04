import requests
import json
import argparse




def analyser_commande():
    """
    Générer un interpréteur de commande.

    Returns:
        Un objet Namespace tel que retourné par parser.parse_args().
        Cet objet aura l'attribut «symboles» représentant la liste des
        symboles à traiter, et les attributs «début», «fin» et «valeur»
        associés aux arguments optionnels de la ligne de commande.
    """
    parser = argparse.ArgumentParser(description='Projet pour recupper des arguments de valeurs boursiers')

    parser.add_argument('entreprise', type=str, help='nom de entreprise')
    parser.add_argument('date_debut', type=str, help='date debut')
    parser.add_argument('date_fin', type=str, help='date de fin')

    return parser.parse_args()

# utilisation de la fonction analyser_commande
get_parameters=analyser_commande()
# utilisation url 
symbole =get_parameters.entreprise
url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

params = {
    'début': get_parameters.date_debut,
    'fin': get_parameters.date_fin,
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