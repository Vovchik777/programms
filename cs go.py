import random
import time
from colorama import Back
from colorama import Style
from colorama import init, Fore

init(autoreset=True)
chel = ''
chel_hp = ['Тот ', 'не Тот ', 'не Тот ', 'не Тот ']
pawp = ['Попал','Попал','Попал','Попал','Попал','Попал','Попал','Попал','Попал','Не попал']
pg = ['Попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал','Не попал']
p50 = ['Попал ', 'Не попал']
uron = ['Нанесли ', 'Не нанесли']
bon_ak = 20
bon_m = 30
pak = ['Попал ', 'Не попал', 'Не попал', 'Не попал']
raskidka = ['Нанесли урон ', 'Не нанесли урон ', 'Не нанесли урон ', 'Не нанесли урон ', 'Не нанесли урон ']
gun = {
    "t": [
        {'name': 'p200', 'price': 300, 'damage': 34, 'bonuse': ''},
        {'name': 'tec9', 'price': 500, 'damage': 56, 'bonuse': ''},
        {'name': 'desert eagle', 'price': 700, 'damage': 100, 'bonuse': ''},
        {'name': 'SSG 08', 'price': 1700, 'damage': 80, 'bonuse': ''},
        {'name': 'ak-47', 'price': 2700, 'damage': 40, 'bonuse': 'Стреляет 20 патронами'},
        {'name': 'AWP', 'price': 4750, 'damage': 450, 'bonuse': '90% попадание'}

    ],
    "ct": [
        {'name': 'p250', 'price': 300, 'damage': 20, 'bonuse': ''},
        {'name': 'Five-Seven', 'price': 350, 'damage': 60, 'bonuse': ''},
        {'name': 'R8', 'price': 600, 'damage': 89, 'bonuse': ''},
        {'name': 'SSG 08', 'price': 1700, 'damage': 80, 'bonuse': ''},
        {'name': 'M4A1-S', 'price': 2900, 'damage': 20, 'bonuse': 'Стреляет 30 патронами'},
        {'name': 'AWP', 'price': 4750, 'damage': 450, 'bonuse': '90% попадание'}]
}
t = 0
ct = 0
svet = ["Red", "Blue", "Yellow"]
vib = input('За кого играешь:' + Fore.RED + 't' + Fore.BLUE + ',ct').strip()
if vib not in gun:
    print('Такого нету')
    exit(1)
bal = 800
inventory = []


def smert(txt):
    global bal, ct, t, pok
    print(Back.BLACK + Fore.RED + 'Тебя' + Fore.LIGHTRED_EX + ' убили' + Fore.RED + f' {txt}')
    time.sleep(1.5)
    for i in range(10, 0, -1):
        time.sleep(1)
        x = random.choice(svet)
        if x == "Yellow":
            print(Fore.YELLOW + f'следущий раунд через {i} сек')
        elif x == "Blue":
            print(Fore.BLUE + f'следущий раунд через {i} сек')
        else:
            print(Fore.RED + f'следущий раунд через {i} сек')
    bal += 1700
    print(bal)
    pok = ''
    inventory.clear()
    if vib == 't':
        ct += 1
        print('У контр-терроров ' + str(ct) + ' очков!')
    else:
        t += 1
        print('У терроров ' + str(t) + ' очков!')
    print(bal)


def obsterl(oru):
    global bal, b, hpchela, hp_vraga, chel
    if b == 'Попал ' and gun[vib][pok]['damage'] >= 100:
        bal += 300
        print('Попал и убил')
        print('+300$')
        print(bal)
    elif b == 'Попал ' and gun[vib][pok]['damage'] < 100:
        print('Попал')
        print('У него осталось ' + str(100 - gun[vib][pok]['damage']) + ' хп')
        hp_vraga = 100 - gun[vib][pok]['damage']
        chel = 'Попадание'
    else:
        print('Не попал')
        # hp = random.choice(uron)
        # if hp == 'Нанесли':
        nanesli = random.randint(1, hpchela)
        hpchela -= nanesli
        print('тебе нанесли '+str(nanesli)+' урона')
        if hpchela <= 0:
            time.sleep(1.5)
            # перестрелка
            smert('пулей')



def bonstrel(oru, bon):
    global hpchela, bal
    d = 0
    nanesli = random.randint(1, 100)
    if str(bon).isdigit():
        for i in range(0, bon):
            b = random.choice(pak)
            print('Выстрел')
            if b == 'Попал ':
                d += gun[vib][pok]['damage']
                if d >= 100:
                    print('Убил')
                    print('+300$')
                    bal += 300
                    print(bal)
                    break

    else:
        b = random.choice(bon)
        if b == 'Попал':
            print('+150$')
            bal+=150
            print(bal)
        else:
            print('Не попал')
        if hpchela <= 0:
            time.sleep(1.5)
            # перестрелка
            nanesli = random.randint(1, 100)
            hpchela -= nanesli
            if hpchela <= 0:
                smert('пулей')
            else:
                print('тебе нанесли ' + str(nanesli) + ' урона, твои хп - ' + str(hpchela))
while t != 16 or ct != 16:
    hp_vraga = 100
    d = 0
    chel=''
    hpchela = 100
    max_len = 0
    max_bonuse = 0

    for g in gun[vib]:
        if max_len < len(g['name']):
            max_len = len(g['name'])
        if max_bonuse < len(g['bonuse']):
            max_bonuse = len(g['bonuse'])
    max_len += 3
    if inventory == []:
        print(bal)
        print(Back.BLACK + Fore.MAGENTA + 'Что покупаешь?:' + Style.RESET_ALL)
        print(f"{'': >{max_len / 2+0.3}} " + Fore.BLACK + Back.RED + 'Название',
              f"{'': >{max_len / 3+1}}" + Fore.BLACK + Back.RED + "Цена",
              f"{'': >{max_len / 4 + 5.1}}" + Fore.BLACK + Back.RED + "Дамаг",
              f"{'': >{max_len / 4 + 10}}" + Fore.BLACK + Back.RED + "Бонус")
        for i, g in enumerate(gun[vib]):
            print(
                f"{(i + 1): >2} {g['name']:_<{max_len}} | {g['price']:^10} | {g['damage']:^10} | {g['bonuse']:^{max_bonuse}}|")
        pok = int(input()) - 1
        try:
            if bal < gun[vib][pok]['price']:
                print('Не хватает денег')
                continue
            bal -= gun[vib][pok]['price']
        except IndexError:
            print('Такого оружия нету')
            continue
        print(bal)
        inventory.append(gun[vib][pok]['name'])
    else:
        pokupka = input('У тебя в инвентаре есть:' + Fore.RED + str(
            inventory) + Style.RESET_ALL + "Хочешь заменить или добавить???")
        if pokupka == 'da':
            g = input('заменить или добавить?????\n')
            if g == 'заменить':
                inventory.clear()
                print(Back.BLACK + Fore.MAGENTA + 'Что покупаешь?:' + Style.RESET_ALL)
                print(f"{'': >{max_len / 2}} " + Fore.BLACK + Back.RED + 'Название',
                      f"{'': >{max_len / 3}}" + Fore.BLACK + Back.RED + "Цена",
                      f"{'': >{max_len / 4 + 5}}" + Fore.BLACK + Back.RED + "Дамаг")
                for i, g in enumerate(gun[vib]):
                    print(
                        f"{(i + 1): >2} {g['name']:_<{max_len}} | {g['price']:^10} | {g['damage']:^10} | {g['bonuse']:^{max_bonuse}}|")
                pok = int(input()) - 1
                if bal < gun[vib][pok]['price']:
                    print('Не хватает денег')
                    continue
                bal -= gun[vib][pok]['price']
                print(bal)
                inventory.append(gun[vib][pok]['name'])
            else:
                print(bal)
                print(Back.BLACK + Fore.MAGENTA + 'Что покупаешь?:' + Style.RESET_ALL)
                print(f"{'': >{max_len / 2}} " + Fore.BLACK + Back.RED + 'Название',
                      f"{'': >{max_len / 3}}" + Fore.BLACK + Back.RED + "Цена",
                      f"{'': >{max_len / 4 + 5}}" + Fore.BLACK + Back.RED + "Дамаг")
                for i, g in enumerate(gun[vib]):
                    print(
                        f"{(i + 1): >2} {g['name']:_<{max_len}} | {g['price']:^10} | {g['damage']:^10} | {g['bonuse']:^{max_bonuse}}|")
                pok = int(input()) - 1
                if bal < gun[vib][pok]['price']:
                    print('Не хватает денег')
                    continue
                bal -= gun[vib][pok]['price']
                print(bal)
                inventory.append(gun[vib][pok]['name'])
    time.sleep(1)
    print('Начало раунда')
    time.sleep(2.5)
    print('Выстрел')
    b = random.choice(p50)
    if 'ak-47' in inventory:
        bonstrel('ak-47',bon = bon_ak)
    elif 'M4A1-S' in inventory:
        bonstrel('M4A1-S',bon = bon_m)
    elif 'AWP' in inventory:
            bonstrel('AWP',pawp)
    else:
        obsterl(inventory[0])
    rask = random.choice(raskidka)
    if rask == 'Нанесли урон ':
        hpchela -= random.randint(1, hpchela)
        if hpchela <= 0:
            smert('гранатой')
            continue
            # смерть от раскидки
        else:
            time.sleep(1.5)
            print('По тебе попали раскидкой, твои хп - ' + str(hpchela))
    else:
        time.sleep(1.5)
        print('Тебе повезло по тебе не попали раскидкой!')
    if chel == 'Попадание':
        chel1 = random.choice(chel_hp)
        if chel1 == 'Тот ':
            print('Это тот чувак , у него ' + str(hp_vraga) + ' хп')
            obsterl(inventory[0])
    else:
        time.sleep(2.5)
        print('Выстрел')
        b = random.choice(p50)
        if 'ak-47' in inventory:
            bonstrel('ak-47', bon=bon_ak)
        elif 'M4A1-S' in inventory:
            bonstrel('M4A1-S', bon=bon_m)
        elif 'AWP' in inventory:
            bonstrel('AWP', pawp)
        else:
            obsterl(inventory[0])
        # if gun[vib][pok]['bonuse']!= '':
        #     bonstrel()
        # obsterl(inventory[0])
    bal += 3200
    print(bal)
    if vib == 't':
        t += 1
        print('У терроров ' + str(t) + ' очков!')
    else:
        ct += 1
        print('У контр-терроров ' + str(ct) + ' очков!')
    continue

    # urn=input('Завершить игру?:\n')
    # if urn == 'да':
    #     exit()
