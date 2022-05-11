import sqlite3
from db import create_database
from rich.console import Console
from rich.table import Table
import subprocess


page = 1

con = sqlite3.connect('database.db')
cur = con.cursor()

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
        print("   3) Voir la cargaison des bateaux")

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

    if(page == 2):
        if(r == 1):
            pass
        elif(r == 2):
            cur.execute("SELECT numImportation, nomMarchandise, poidsMarchandise, dateArriveeImportation, numQuai, matriculeBateau FROM Importations JOIN Conteneurs USING(numConteneur) JOIN TypeMarchandises USING(numTypeMarchandise)")
            rows = cur.fetchall()
            show_query_results(rows, 1)

    elif(page == 6):
        if(r == 1):
            cur.execute("SELECT matriculeBateau, nomBateau FROM Bateaux")
            rows = cur.fetchall()
            show_query_results(rows, 2)
        
        elif(r == 2):
            cur.execute("SELECT matriculeBateau, nomBateau FROM Bateaux WHERE matriculeBateau NOT IN (SELECT matriculeBateau FROM Importations)")
            rows = cur.fetchall()
            show_query_results(rows, 3)

        elif(r == 3):
            cur.execute("SELECT matriculeBateau, nomBateau, nomMarchandise, poidsMarchandise FROM Importations JOIN Conteneurs USING(numConteneur)")
            rows = cur.fetchall()
            show_query_results(rows, 3)

    return page


def show_query_results(rows, query_id):

    if(query_id == 1):

        table = Table(title="Toutes les importations")
        table.add_column("Numéro")
        table.add_column("Marchandise")
        table.add_column("Poids")
        table.add_column("Date d'arrivée")
        table.add_column("Quai")
        table.add_column("Matricule bateau")

        for row in rows:
            table.add_row(str(row[0]), row[1], str(row[2]), row[3], str(row[4]), row[5])

    elif(query_id == 2):
        table = Table(title="Tous les bateaux")
        table.add_column("Nom")
        table.add_column("Matricule")

        for row in rows:
            table.add_row(row[1], row[0])

    elif(query_id == 3):
        table = Table(title="Tous les bateaux qui n'ont pas de livraison en cours")
        table.add_column("Nom")
        table.add_column("Matricule")

        for row in rows:
            table.add_row(row[1], row[0])


    console = Console()
    console.print(table)

    input("Appuyez sur la touche entrée pour continuer...")


def get_console_width():
    tput = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
    return int(tput.communicate()[0].strip())


def main():

    print(get_console_width())

    break_ = False
    while not(break_):

        display_menu(page)
        response = input()
        treat_user_response(response)
    

#create_database(cur)

main()