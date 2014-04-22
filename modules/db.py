'''
Created on 17 avr. 2014

@author: admin
'''
# Utilisation d une petite base de donnees acceptant les requetes SQL
 
import sqlite3



def consoleDB():
    baseDonn = sqlite3.connect("edx-logs.db")
    cur = baseDonn.cursor()
    while 1:
        print("Veuillez entrer votre requete SQL  ou  Enter  pour terminer ")
        print("--> Exemple : 'select count(country), country from results group by country' ")
        requete = input()
        if requete =="":
            break
        try:
            cur.execute(requete)       # execution de la requete SQL
        except:
            print('   Requete SQL incorrecte ')
        else:
            for enreg in cur:     # Affichage du resultat
                print(enreg)
        print()
    choix = input("Confirmez vous lenregistrement de letat actuel  o n    ")
    if choix[0] == "o" or choix[0] == "O":
        baseDonn.commit()
    else:
        baseDonn.close()