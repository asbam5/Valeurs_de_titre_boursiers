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


def produire_historique(symbole ,debut,fin,valeur='fermeture'):
    """
    affichage des valeurs boursiers.

    Returns:
        Note module phase1 produit l'affichage des historiques des symboles
        spécifiés sur la ligne de commande en respectant le format d'affichage
        décrit par l'énoncé du projet.
        Un object de type texte (str) avec les structures correspondant.

        exemple 1:
            python phase1.py -v=volume -f=2019-02-22 goog
            titre=goog: valeur=volume, début=datetime.date(2019, 2, 22),
            fin=datetime.date(2019, 2, 22) [(datetime.date(2019, 2, 22),
            1049545)]
        exemple 2:
            python phase1.py -d=2019-02-18 -f=2019-02-24 goog
            titre=goog: valeur=fermeture, début=datetime.date(2019, 2, 18), fin=
            datetime.date(2019, 2, 24)
            [(datetime.date(2019, 2, 19), 1118.56), (datetime.date(2019, 2, 20), 1113.8),
            (datetime.date(2019, 2, 21), 1096.97), (datetime.date(2019, 2, 22), 1110.37)]
    """
    list_date=[]

    answer_out=""
    for elemnt_symbole in symbole:

        url = f'https://pax.ulaval.ca/action/{elemnt_symbole}/historique/'
        if debut is None and fin is not None:
            debut=fin
        # check is date de fin n'existe pas il prend today
        if  debut is not None and fin is None:
            fin=str(datetime.date.today())
        list_date.append(datetime.datetime.strptime(debut,'%Y-%m-%d').date())
        list_date.append(datetime.datetime.strptime(fin,'%Y-%m-%d').date())

        params = {
            'début': debut,
            'fin': fin,
        }
        réponse = requests.get(url=url, params=params, timeout=60)
        réponse = json.loads(réponse.text)
        reponse_value=[]
        for key in réponse['historique'].keys():
            reponse_value.append((datetime.datetime.strptime(key,'%Y-%m-%d').date(),
                                  réponse['historique'][key][valeur]))
        answer=""
        answer=f"titre={elemnt_symbole}: valeur={valeur}, début="
        answer+=f"datetime.date({list_date[0].year}, {list_date[0].month}, {list_date[0].day}), "
        answer+=f"fin=datetime.date({list_date[1].year}, {list_date[1].month}, {list_date[1].day})"
        reponse_value.reverse()
        answer=answer+"\n"+str(reponse_value)
        answer_out=answer_out+"\n"+answer
    return answer_out



get_parameters=analyser_commande()
reponse=produire_historique(get_parameters.symbole,get_parameters.début,get_parameters.fin,get_parameters.valeur)

print(reponse)
