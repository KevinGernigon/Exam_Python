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


premier_mot = ["G", "I","R","A","F","E"]
second_mot = ["H","O","S","T","I","E"]
troisieme_mot = ["D","R","A","G","O","N"]
quatrieme_mot = ["C", "O","R","A","I","L"]
cinquieme_mot = ["C","H","E","V","A","L"]
sixieme_mot = ["C","A","S","T","O","R"]
septieme_mot = ["A","L","C","Y","O","N"]
huitieme_mot = ["O","I","S","E","A","U"]
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
    
def trouvelettre (tableau_mot, mot_joueur) :
    for i in range (0,6) :
        if (tableau_mot[i] == mot_joueur[i]) :
            print(Back.RED + mot_joueur[i], end = " ")
        else :
            print(Back.BLUE + mot_joueur[i], end = " ")
    return
    
def comptelettre (tableau_mot, lettre) :
    compteur_lettre = 0
    for i in range (0,6) :
        if (tableau_mot[i] == lettre) :
            compteur_lettre = compteur_lettre +1
    return compteur_lettre     

for i in range (0,9) :
    mot_joueur = input("\n Veuillez saisir un mot en majuscules \n")
    trouvelettre(mot_jeu, mot_joueur)
    if (mot_jeu == mot_joueur) :
        print("Vous avez gagner la partie !")
        break
        
            
input()