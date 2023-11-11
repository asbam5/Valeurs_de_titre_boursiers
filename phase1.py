"""Module d'affichage des valeurs boursiers."""
import json
import argparse
import datetime
import requests



def analyser_commande():
    """
    Générer un interpréteur de commande.

    Returns:
        Un objet Namespace tel que retourné par parser.parse_args().
        Cet objet aura l'attribut «symboles» représentant la liste des
        symboles à traiter, et les attributs «début», «fin» et «valeur»
        associés aux arguments optionnels de la ligne de commande.
    """
    parser = argparse.ArgumentParser(
    description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.')

    parser.add_argument('symbole', type=str,nargs='+',help="Nom d'un symbole boursier")
    parser.add_argument('-d','--début',metavar='DATE', type=str, 
    help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f','--fin',metavar='DATE', type=str,
    help='Date recherchée la plus récente (format: AAAA-MM-JJ)')
    parser.add_argument('-v','--valeur',default='fermeture',type=str,
    choices=['fermeture', 'ouverture', 'min', 'max','volume'],
    help='La valeur désirée (par défaut: fermeture)')
    return parser.parse_args()


def produire_historique():
    "affichage des valeurs boursiers"
    list_date=[]
    get_parameters=analyser_commande()

    answer_out=""
    for elemnt_symbole in get_parameters.symbole:

        url = f'https://pax.ulaval.ca/action/{elemnt_symbole}/historique/'
        if get_parameters.début is None and get_parameters.fin is not None:
            get_parameters.début=get_parameters.fin
        # check is date de fin n'existe pas il prend today
        if  get_parameters.début is not None and get_parameters.fin is None:
            get_parameters.fin=str(datetime.date.today())
        list_date.append(datetime.datetime.strptime(get_parameters.début,'%Y-%m-%d').date())
        list_date.append(datetime.datetime.strptime(get_parameters.fin,'%Y-%m-%d').date())

        params = {
            'début': get_parameters.début,
            'fin': get_parameters.fin,
        }
        réponse = requests.get(url=url, params=params, timeout=60)
        réponse = json.loads(réponse.text)
        reponse_value=[]
        for key in réponse['historique'].keys():
            reponse_value.append((datetime.datetime.strptime(key,'%Y-%m-%d').date(),
                                  réponse['historique'][key][get_parameters.valeur]))
        answer=""
        answer=f"titre={elemnt_symbole}: valeur={get_parameters.valeur}, début="
        answer+=f"datetime.date({list_date[0].year}, {list_date[0].month}, {list_date[0].day}), "
        answer+=f"fin=datetime.date({list_date[1].year}, {list_date[1].month}, {list_date[1].day})"
        reponse_value.reverse()
        answer=answer+"\n"+str(reponse_value)
        answer_out=answer_out+"\n"+answer
    return answer_out

reponse=produire_historique()
print(reponse)
