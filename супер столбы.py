import random
import time
from colorama import *
slovo = []
lava = []
while True:
    def color(list,list1):
        if list in list1:
            print('│←ты')
            for i in list:
                print(Back.BLACK + f'{i}' + Style.RESET_ALL)
    def perebor(text):
        print(Fore.MAGENTA + '¯' * 100 + Style.RESET_ALL)
        for i in text:
            if'*' not in i :
                slovo.append(i)
            else:
                lava.append(Back.RED+Fore.RED+'*'+Back.RESET+'←Лава'+Style.RESET_ALL)
                if len(lava) >= len(slovo):
                    print('Ты погиб')
                    exit()
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'magenta', 'amaranthine', 'pink', 'lightblack', 'lightblue',
              'cyan', 'lightred']
    plants = ['tree','flower','blossom','floret','bush',]


    svet = input('Цвет:\n')
    color(svet,colors)
    perebor(svet)
    start = time.time()
    while svet not in colors:
        svet = input( '\nЦвет:\n')
        print(start)
        end = time.time() - start
        if end >= 10:
            print('Ты не успел')
            break
    #color(list = svet,list1= colors)
        perebor(svet)
    svet1 = list(svet)
    ind = random.randint(1,len(svet1)-2)
    print(Fore.MAGENTA+'¯'*100+Style.RESET_ALL)
    for i in range(-ind,0):
        svet1[i] = Back.RED+Fore.RED+'*'+Back.RESET+'←Лава'+Style.RESET_ALL
        svet2 = svet1
    print('│←ты')
    for i in svet1:
        print(Back.BLACK + f'{i}' + Style.RESET_ALL)
    perebor(text = svet2)
    rast = input('Растение:\n')
    rast1 = list(rast)
    while rast not in plants:
        input('Растение:\n')
    ind = random.randint(1,len(rast)-2)
    print(Fore.MAGENTA+'¯'*100+Style.RESET_ALL)
    for i in range(-ind,0):
        rast1[i] = Back.RED+Fore.RED+'*'+Back.RESET+'←Лава'+Style.RESET_ALL
        rast2 = rast1
    perebor(text = rast2)
    print('│←ты')
    for i in slovo:
        print(i)
    for r in lava:
        print(r)