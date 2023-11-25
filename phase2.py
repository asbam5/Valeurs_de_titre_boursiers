"""Module programme principal"""
import datetime
from bourse import Bourse




def main():
    obj1=Bourse()
    
    symbole="goog"
    date=datetime.datetime.strptime('2023-10-14','%Y-%m-%d').date()
    print(obj1.prix(symbole,date).split('\n')[2])
    
main()