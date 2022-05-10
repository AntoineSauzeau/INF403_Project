import sqlite3
from db import create_database

page = 1

def display_menu(page):

    print("---------------")
    
    if(page==1):
        print("Que voulez vous faire ?")
        print("   1) Jeter un coup d'oeil aux importations")
        print("   2) Jeter un coup d'oeil aux stocks")
        print("   3) Jeter un coup d'oeil à l'état des entrepôts")
        print("   4) Jeter un coup d'oeil aux quais")
        print("   5) Jeter un coup d'oeil aux bateaux")

    elif(page==2):
        print("Menu : Importation")
        print("Que voulez vous faire ?")
        print("   1) Voir les importations qui arrivent aujourd'hui")
        print("   2) Voir toutes les importations")
    elif(page == 3):
        print("Menu : Stocks")
        print("Que voulez vous faire ?")
        print("   1) Voir l'entièreté de ce qui est stocké")
        print("   2) Voir ce qui est stocké par entrepôt")
        print("   3) Voir ce qui est stocké par secteur")
        print("   4) Voir ce qui est stocké après arrivée des importations")
    
    elif(page == 4):
        print("Menu : Etats des entrepôts")
        print("Que voulez vous faire ?")
        print("   1) Place restante par entrepôt")
        print("   2) Place restante par secteur")

    elif(page == 5):
        print("Menu : Quais")
        print("Que voulez vous faire ?")
        print("   1) Nombre d'importation programmées par quais")

    elif(page == 6):
        print("Menu : Bateaux")
        print("Que voulez vous faire ?")
        print("   1) Voir la liste des bateaux")
        print("   2) Voir les bateaux qui n'ont pas de livraison en cours")
        print("   3) Voir la cargaison d'un bateau en particulier")

    if(page != 1):
        print("   -) Retour")
    print("   --) Quitter le programme")

    print("---------------")

def treat_user_response(r):

    global page   

    if(r == "--"):
        exit()
    elif(r == "-"):
        if(page >= 2 and page <= 6):
            page = 1

    else:
        r = int(r)
 
    if(page == 1):
        if(r == 1):
            page = 2
        elif(r == 2):
            page = 3
        elif(r == 3):
            page = 4
        elif(r == 4):
            page = 5
        elif(r == 5):
            page = 6

    return page



def main():

    break_ = False
    while not(break_):

        display_menu(page)
        response = input()
        treat_user_response(response)
    

con = sqlite3.connect('database.db')
cur = con.cursor()

#create_database(cur)

main()