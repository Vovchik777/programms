import random
import time
from colorama import *

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'magenta', 'amaranthine', 'pink', 'lightblack', 'lightblue',
          'cyan', 'lightred']

svet = list(input('Цвет:\n'))


def color():
    if svet in colors:
        print('│←ты')
        for i in svet:
            print(Back.BLACK + f'{i}' + Style.RESET_ALL)


while svet not in colors:
    svet = input('Цвет:\n')
color()
