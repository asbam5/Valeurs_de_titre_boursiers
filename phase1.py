import requests
import json
import argparse
import datetime




def analyser_commande():
    """
    Générer un interpréteur de commande.

    Returns:
        Un objet Namespace tel que retourné par parser.parse_args().
        Cet objet aura l'attribut «symboles» représentant la liste des
        symboles à traiter, et les attributs «début», «fin» et «valeur»
        associés aux arguments optionnels de la ligne de commande.
    """
    parser = argparse.ArgumentParser(description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.')

    parser.add_argument('symbole', type=str, help="Nom d'un symbole boursier")
    parser.add_argument('-d','--début',metavar='DATE', type=str, help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f','--fin',metavar='DATE', type=str, help='Date recherchée la plus récente (format: AAAA-MM-JJ)')
    parser.add_argument('-v','--valeur',default='fermeture',type=str, choices=['fermeture', 'ouverture', 'min', 'max','volume'], help='La valeur désirée (par défaut: fermeture)')
    return parser.parse_args()


def affichage():
    "affichage des valeurs boursiers"
    list_date=[]
    get_parameters=analyser_commande()
    url = f'https://pax.ulaval.ca/action/{get_parameters.symbole}/historique/'
    

    if get_parameters.début==None and get_parameters.fin!=None:
        get_parameters.début=get_parameters.fin 
    #### todo 1 definir la plage des dates  exemple 2019-03-01 a 2019-04-03 et la mettre dans la variables liste_date
    debut=datetime.datetime.strptime(get_parameters.début,'%Y-%m-%d')
    fin=datetime.datetime.strptime(get_parameters.fin,'%Y-%m-%d')
    list_date.append(debut.date())
    list_date.append(fin.date())
    #print(datetime.date(get_parameters.début[0:3],get_parameters.début[4:5], get_parameters.début[6:-1]))
    #print(datetime.date(int(get_parameters.début[0:4]),int(get_parameters.début[5:7]),int(get_parameters.début[8:])))
    #### todo 2 verifier que si 2 date sont differen    
    
    params = {
        'début': get_parameters.début,
        'fin': get_parameters.fin,
    }
    
    
    #####  Todo 3 transformer les date en type datetime.date
    réponse = requests.get(url=url, params=params)
    réponse = json.loads(réponse.text)
    reponse_value=réponse['historique']['2019-02-22'][get_parameters.valeur]
    reponse_text_fin="titre="+get_parameters.symbole+": valeur="+get_parameters.valeur+", début="+str(list_date[0])+", fin="+str(list_date[-1])
    reponse_fin=[(list_date,reponse_value)]
    
    print(reponse_text_fin,'\n',reponse_fin)
    return reponse_text_fin,reponse_fin


affichage()

#print(get_parameters)
"""
# utilisation de la fonction analyser_commande
get_parameters=analyser_commande()
# utilisation url 
symbole =get_parameters.symbole
url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

params = {
    'début': get_parameters.début,
    'fin': get_parameters.fin,
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
    """
