from colorama import init
init()
from colorama import Fore, Back, Style
import random
#print(Fore.RED + 'some red text', end=" ")
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
#input()


premier_mot = ["A", "G","N","E","A","U"]
second_mot = ["B","I","P","E","D","E"]
troisieme_mot = ["A","L","P","A","G","A"]
quatrieme_mot = ["M", "E","D","U","S","E"]
cinquieme_mot = ["C","O","Y","O","T","E"]
sixieme_mot = ["E","P","O","N","G","E"]
septieme_mot = ["L", "I","E","V","R","E"]
huitieme_mot = ["O","C","E","L","O","T"]
neuvieme_mot = ["P","O","U","L","E","T"]
dixieme_mot = ["O","U","R","S","I","N"]

mot_alea_joueur = random.randrange(0,11)

if (mot_alea_joueur == 1):
    mot_jeu = premier_mot
    
if (mot_alea_joueur == 2):
    mot_jeu = second_mot
    
if (mot_alea_joueur == 3):
    mot_jeu = troisieme_mot
    
if (mot_alea_joueur == 4):
    mot_jeu = quatrieme_mot
    
if (mot_alea_joueur == 5):
    mot_jeu = cinquieme_mot
    
if (mot_alea_joueur == 6):
    mot_jeu = sixieme_mot
    
if (mot_alea_joueur == 7):
    mot_jeu = septieme_mot

if (mot_alea_joueur == 8):
    mot_jeu = huitieme_mot

if (mot_alea_joueur == 9):
    mot_jeu = neuvieme_mot

if (mot_alea_joueur == 10):
    mot_jeu = dixieme_mot
   
def lettre_mal_placee (tableau_mot, mot_joueur) :
    for i in range (0,6):
        if (tableau_mot[i] == mot_joueur[i]):
            pass
        else :
            retient_lettre = mot_joueur[i]
            if (comptelettre(tableau_mot, mot_joueur[i]) > 0 and trouvelettremalplacee(tableau_mot, mot_joueur[i]) == True) :                
                for i in range (0, 6):
                    if (tableau_mot[i] == retient_lettre):
                        print(Back.GREEN + mot_joueur[i], end = " ")
            else :
                print(mot_joueur[i], end = " ")

def trouvelettremalplacee(tableau_mot, lettre):
    for i in range (0,6):
        if (tableau_mot[i] == lettre):
            return True
        else : 
            return False

def trouvelettre (tableau_mot, mot_joueur) :
    for i in range (0,6) :
        if (tableau_mot[i] == mot_joueur[i]) :
            print(Back.RED + mot_joueur[i], end = " ")
        else :
            print(Back.BLUE + mot_joueur[i], end = " ")
    return i
    
def comptelettre (tableau_mot, lettre) :
    compteur_lettre = 0
    for i in range (0,6) :
        if (tableau_mot[i] == lettre) :
            compteur_lettre = compteur_lettre +1
    return compteur_lettre
    
for i in range (0,9) :
 #mot_joueur = input("Veuillez entrer un mot")
    mot_joueur = input("Veuillez entrer un mot")
    trouvelettre(premier_mot, mot_joueur)   
    lettre_mal_placee(premier_mot, mot_joueur)

#comptelettre(mot_jeu, "A")
    
#trouvelettre(premier_mot)
input()