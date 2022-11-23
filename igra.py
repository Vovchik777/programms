import sys

from colorama import init, Fore
from colorama import Back
from colorama import Style
import time

init(autoreset=True)
from random import randint
from termcolor import colored

igr1 = []
igr2 = []
name1 = input('Имя 1 игрока:\n')
name2 = input('Имя 2 игрока:\n')
while len(igr1) < 10 or len(igr2) < 10:
    print(Style.RESET_ALL)
    br = input('Введите * чтобы начать:\n')
    if br == '*':
        b1 = randint(1, 10)
        print(Fore.BLUE +str(b1))
        b2 = randint(1, 10)
        print( Fore.RED +str(b2))
        if b1 > b2:
            igr1 += '🐞'
        elif b2 > b1:
            igr2 += '🐞'
        else:
            print('Перебросьте кубик')
        print('количество баллов у игрока  ' + name1 + Back.BLACK + Fore.BLUE + str(igr1), Fore.BLUE + str(len(igr1)))
        print('количество баллов у игрока ' + name2 + Back.BLACK + Fore.RED + str(igr2), Fore.RED + str(len(igr2)))

    count=0
    if len(igr2) >= 10 or len(igr1) >= 10:
        if len(igr1) > len(igr2):
            print('ВЫИГРАЛ ИГРОК ' + name1)
        elif len(igr2) > len(igr1):
            print('ВЫИГРАЛ ИГРОК ' + name2)
        break
    elif br == 'stop':
        for i in range(randint(1,100)):
            count+=1
            print(Back.RED + Fore.RED + "\r"+Fore.LIGHTCYAN_EX+"Конец"+Fore.LIGHTBLUE_EX+" игры", end="")
            time.sleep(0.2)
            print("\r          ", end="")
            time.sleep(0.2)
        print(count)

        # Back.BLACK+
        # print(Back.BLACK+Fore.RED+"К ",end="")
        # time.sleep(0.5)
        # print(Back.BLACK+Fore.YELLOW+'О ',end='')
        # time.sleep(0.5)
        # print(Back.BLACK+Fore.RED+'Н ',end="")
        # time.sleep(0.5)
        # print(Back.BLACK+Fore.YELLOW+'Е ',end='')
        # time.sleep(0.5)
        # print(Back.BLACK+Fore.RED+'Ц ', end='')

        exit()
