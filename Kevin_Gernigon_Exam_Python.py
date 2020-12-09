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

def trouvelettre (tableau_mot) :
    for i in range (0,6) :
        if (premier_mot[i] == "A") :
            print(i)
    return i
    
trouvelettre(premier_mot)
input()