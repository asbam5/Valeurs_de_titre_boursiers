"""Module bourse.py"""

import datetime
from phase1 import produire_historique


class Bourse:
    def __init__(self):
        pass

    def prix(self,symbole, date):
        """
        affichage des prix.

        Returns:
        """
        if not isinstance(symbole, str):
            raise TypeError("symbole n'est pas string")
        if not isinstance(date, datetime.date):
            raise TypeError("date n'est pas datetime.date")
        valeur=produire_historique([symbole], f"{date.year}-{date.month}-{date.day}",None)
        ## date de fermeture la plus recente disponible (je retourne en arriere de 7 jours)
        if valeur.split('\n')[2]=="[]":
            valeur=produire_historique([symbole], f"{date.year}-{date.month}-{date.day-7}",f"{date.year}-{date.month}-{date.day}")
        
        #valeur=valeur.split('\n')[2].split(',')[3].replace(')]','')+"$"
        return valeur
