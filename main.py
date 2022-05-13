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
        print("   1) Toutes les importations programmées d'un quai")

    elif(page == 6):
        print("Menu : Bateaux")
        print("Que voulez vous faire ?")
        print("   1) Voir la liste des bateaux")
        print("   2) Voir les bateaux qui n'ont pas de livraison en cours")
        print("   3) Voir la cargaison d'un bateau")

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

    elif(page == 2):
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
            id_boat = input("Matricule du bateau : ")
            cur.execute("SELECT matriculeBateau, nomBateau, nomMarchandise, poidsMarchandise FROM Bateaux JOIN Importations USING(matriculeBateau) JOIN Conteneurs USING(numConteneur) JOIN TypeMarchandises USING(numTypeMarchandise) WHERE matriculeBateau='NDTFMYS2'")
            rows = cur.fetchall()
            show_query_results(rows, 4)

    elif(page == 5):
        if(r == 1):
            quai_number = input("Numéro du quai : ")
            cur.execute("SELECT numConteneur, dateArriveeImportation, matriculeBateau FROM Importations WHERE numQuai="+quai_number)
            rows = cur.fetchall()
            show_query_results(rows, 5)

    elif(page == 4):
        if(r == 1):
            cur.execute("SELECT numEntrepot, secteurEntrepot, tailleEntrepot, tailleEntrepot - COUNT(numEntrepot) AS placeRestante FROM Entrepots JOIN StockEntrepots USING (numEntrepot) GROUP BY (numEntrepot)")
            rows = cur.fetchall()
            show_query_results(rows, 6)

        elif(r == 2):
            pass
            #cur.execute("SELECT secteurEntrepot FROM Entrepots JOIN StockEntrepots USING (numEntrepot) GROUP BY (secteurEntrepot)")

    elif(page == 3):
        if(r == 1):
            cur.execute("SELECT numConteneur, nomMarchandise, poidsMarchandise, numEntrepot, secteurEntrepot FROM Entrepots JOIN StockEntrepots USING(numEntrepot) JOIN Conteneurs USING(numConteneur) JOIN TypeMarchandises USING(numTypeMarchandise) ORDER BY numEntrepot ASC")
            rows = cur.fetchall()
            show_query_results(rows, 7)
        
        elif(r == 2):
            num_entrepot = input("Numéro de l'entrepôt : ")
            cur.execute("SELECT numEntrepot, numConteneur, nomMarchandise, poidsMarchandise FROM Entrepots JOIN StockEntrepots USING(numEntrepot) JOIN Conteneurs USING(numConteneur) JOIN TypeMarchandises USING(numTypeMarchandise) WHERE numEntrepot="+num_entrepot)
            rows = cur.fetchall()
            show_query_results(rows, 8)

        elif(r == 3):
            secteur_name = input("Secteur : ")
            cur.execute("SELECT secteurEntrepot, numConteneur, nomMarchandise, poidsMarchandise, numEntrepot FROM Entrepots JOIN StockEntrepots USING(numEntrepot) JOIN Conteneurs USING(numConteneur) JOIN TypeMarchandises USING(numTypeMarchandise) WHERE secteurEntrepot='"+secteur_name+"' ORDER BY numEntrepot ASC")
            rows = cur.fetchall()
            show_query_results(rows, 9)

    return page


def show_query_results(rows, query_id):

    print(rows)

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
        table = Table(title="Liste des bateaux n'ayant pas de livraison en cours")
        table.add_column("Nom")
        table.add_column("Matricule")

        for row in rows:
            table.add_row(row[1], row[0])

    elif(query_id == 4):
        table = Table(title="Cargaison du bateau \'" + rows[0][1] + "\'")
        table.add_column("Marchandise")
        table.add_column("Poids")

        for row in rows:
            table.add_row(row[2], str(row[3]))

    elif(query_id == 4):
        table = Table(title="Cargaison du bateau " + row[0])
        table.add_column("Marchandise")
        table.add_column("Poids")

        for row in rows:
            table.add_row(row[2], row[3])

    elif(query_id == 5):
        table = Table(title="Importations programmées sur ce quai")
        table.add_column("Numéro du conteneur")
        table.add_column("Date d'arrivée")
        table.add_column("Matricule du bateau")

        for row in rows:
            table.add_row(str(row[0]), row[1], row[2])

    elif(query_id == 6):
        table = Table(title="Place restante par entrepôt")
        table.add_column("Numéro de l'entrepôt")
        table.add_column("Secteur")
        table.add_column("Taille")
        table.add_column("Place restante")

        for row in rows:
            table.add_row(str(row[0]), row[1], str(row[2]), str(row[3]) + " (" + str((row[3] / row[2])*100) + "%)")

    elif(query_id == 7):
        table = Table(title="Inventaire des stocks")
        table.add_column("Identifiant")
        table.add_column("Marchandise")
        table.add_column("Poids")
        table.add_column("Entrepôt")
        table.add_column("Secteur")

        for row in rows:
            table.add_row(str(row[0]), row[1], str(row[2]), str(row[3]), row[4])

    elif(query_id == 8):
        table = Table(title="Inventaire de l'entrepôt " + str(rows[0][0]))
        table.add_column("Identifiant")
        table.add_column("Marchandise")
        table.add_column("Poids")

        for row in rows:
            table.add_row(str(row[1]), row[2], str(row[3]))

    elif(query_id == 9):
        table = Table(title="Inventaire du secteur " + rows[0][0])
        table.add_column("Identifiant")
        table.add_column("Marchandise")
        table.add_column("Poids")
        table.add_column("Entrepôt")

        for row in rows:
            table.add_row(str(row[1]), row[2], str(row[3]), str(row[4]))


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
    


create_database(cur)

main()