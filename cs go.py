import random
import time

from colorama import Back
from colorama import Style
from colorama import init, Fore

init(autoreset=True)
p50 = ['Попал ', 'Не попал']
uron = ['Нанесли ', 'Не нанесли']
raskidka = ['Нанесли урон ', 'Не нанесли урон ', 'Не нанесли урон ', 'Не нанесли урон ', 'Не нанесли урон ']
gun = {
    "t": [
        {'name': 'p200', 'price': 300, 'damage': 34},
        {'name': 'tec9', 'price': 500, 'damage': 56},
        {'name': 'desert eagle', 'price': 700, 'damage': 100},
        {'name': 'SSG 08', 'price': 1700, 'damage': 80}
    ],
    "ct": [
        {'name': 'p250', 'price': 300, 'damage': 20},
        {'name': 'Five-Seven', 'price': 350, 'damage': 60},
        {'name': 'R8', 'price': 600, 'damage': 89},
        {'name': 'SSG 08', 'price': 1700, 'damage': 80}
    ]
}

t = 0
ct = 0
vib = input('За кого играешь:t,ct').strip()
bal = 800
while t != 16 or ct != 16:
    hpchela = 1
    max_name = 0
    for g in gun[vib]:
        if max_name < len(g['name']):
            max_name = len(g['name'])
    max_name += 3
    print(Back.BLACK + Fore.MAGENTA + 'Что покупаешь?:' + Style.RESET_ALL)
    for i, g in enumerate(gun[vib]):
        print(f"{(i + 1): >2} {g['name']:_<{max_name}} | {g['price']:^10} | {g['damage']:^10} |")
    pok = int(input()) - 1
    if bal < gun[vib][pok]['price']:
        print('Не хватает денег')
        continue
    bal -= gun[vib][pok]['price']
    print(bal)
    time.sleep(1)
    print('Начало раунда')
    time.sleep(2.5)
    print('Выстрел')
    b = random.choice(p50)
    if b == 'Попал ' and gun[vib][pok]['damage'] >= 100:
        bal += 300
        print('Попал и убил')
        print('+300$')
        print(bal)
    elif b == 'Попал ' and gun[vib][pok]['damage'] < 100:
        print('Попал')
        print('У него осталось ' + str(100 - gun[vib][pok]['damage']) + ' хп')
    else:
        print('Не попал')
        # hp = random.choice(uron)
        # if hp == 'Нанесли':
        nanesli = random.randint(1, 100)
        hpchela -= nanesli
        if hpchela <= 0:
            print('Тебя убили ')
            for i in range(10, 0, -1):
                time.sleep(1)
                print(f'следущий раунд через {i} сек')
            bal += 1700
            continue
        else:
            print('Тебе нанесли ' + str(nanesli) + ' урона, твои хп  ' + str(hpchela))
    rask = random.choice(raskidka)
    if rask == 'Нанесли урон ':
        hpchela -= random.randint(1, hpchela)
        if hpchela <= 0:
            print('Тебя убили раскидкой, ')
            for i in range(10, 0, -1):
                time.sleep(1)
                print(f'следущий раунд через {i} сек')
            bal += 1700
            continue

        else:
            print('По тебе попали раскидкой, твои хп - ' + str(hpchela))
    else:
        print('Тебе повезло по тебе не попали раскидкой!')
