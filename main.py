import sqlite3

def display_menu(page):

    print("---------------")
    
    if(page==1):
        print("Que voulez vous faire ?")
        print("   1) Jeter un coup d'oeil aux importations")
    elif(page==2):
        print("Menu : Importation")
        print("Que voulez vous faire ?")
        print("   1) Voir les importations qui arrive aujourd'hui")
        print("   2) Voir toutes les importations")

    print("---------------")
    

from db import create_database

con = sqlite3.connect('database.db')
cur = con.cursor()

display_menu(1)

create_database(cur)