from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
#input()


premier_mot = ["A", "G","N","E","A","U"]
second_mot = ["B","I","P","E","D","E"]

def trouvelettre (tableau_mot) :
    for i in range (0,6) :
        if (tableau_mot[i] == mot_joueur[i]) :
            print(Back.RED + mot_joueur[i], end = " ")
    return i
    
def comptelettre (tableau_mot, lettre) :
    compteur_lettre = 0
    for i in range (0,6) :
        if (tableau_mot[i] == lettre) :
            compteur_lettre = compteur_lettre +1
    print(compteur_lettre)
    return compteur_lettre
    
mot_joueur = input("Veuillez entrer un mot")
#trouvelettre(second_mot)

comptelettre(premier_mot, "A")
    
#trouvelettre(premier_mot)
input()