import random
import time

from colorama import Back
from colorama import Style
from colorama import init, Fore

init(autoreset=True)
chel=''
chel_hp=['Тот ','не Тот ','не Тот ','не Тот ']
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
svet=["Red","Blue","Yellow"]
vib = input('За кого играешь:'+Fore.RED+'t'+Fore.BLUE+',ct').strip()
bal = 800
inventory=[]
while t != 16 or ct != 16:
    hpchela = 100
    max_name = 0
    for g in gun[vib]:
        if max_name < len(g['name']):
            max_name = len(g['name'])
    max_name += 3
    if inventory == []:
        print(bal)
        print(Back.BLACK + Fore.MAGENTA + 'Что покупаешь?:' + Style.RESET_ALL)
        print(f"{'': >{max_name/2}} "+Fore.BLACK+Back.RED+'Название' ,f"{'': >{max_name/3}}" +Fore.BLACK+Back.RED+"Цена",f"{'': >{max_name/4+5}}" +Fore.BLACK+Back.RED+"Дамаг")
        for i, g in enumerate(gun[vib]):
            print(f"{(i + 1): >2} {g['name']:_<{max_name}} | {g['price']:^10} | {g['damage']:^10} |")
        pok = int(input()) - 1
        if bal < gun[vib][pok]['price']:
            print('Не хватает денег')
            continue
        bal -= gun[vib][pok]['price']
        print(bal)
        inventory.append(gun[vib][pok]['name'])
    else:
        pokupka=input('У тебя в инвентаре есть:'+Fore.RED+str(inventory)+Style.RESET_ALL+"Хочешь заменить???")
        if pokupka == 'da':
            print(bal)
            print(Back.BLACK + Fore.MAGENTA + 'Что покупаешь?:' + Style.RESET_ALL)
            for i, g in enumerate(gun[vib]):
                print(f"{(i + 1): >2} {g['name']:_<{max_name}} | {g['price']:^10} | {g['damage']:^10} |")
            pok = int(input()) - 1
            inventory.clear()
            inventory.append(gun[vib][pok]['name'])
            print('Теперь у тебя '+str(inventory))
            if bal < gun[vib][pok]['price']:
                print('Не хватает денег')
                continue
            else:
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
        hp_vraga=100-gun[vib][pok]['damage']
        chel='Попадание'
    else:
        print('Не попал')
        # hp = random.choice(uron)
        # if hp == 'Нанесли':
        nanesli = random.randint(1, 100)
        hpchela -= nanesli
        if hpchela <= 0:
            time.sleep(1.5)
            print(Back.BLACK+Fore.RED+'Тебя '+Fore.LIGHTRED_EX+'убили ')
            for i in range(10, 0, -1):
                time.sleep(1)
                x=random.choice(svet)
                if x == "Yellow":
                    print(Fore.YELLOW+f'следущий раунд через {i} сек')
                elif x == "Blue":
                    print(Fore.BLUE + f'следущий раунд через {i} сек')
                else:
                    print(Fore.RED + f'следущий раунд через {i} сек')
            bal += 1700
            print(bal)
            pok=''
            inventory.clear()
            if vib == 't':
                ct+=1
                print('У контр-терроров '+str(ct)+' очков!')
            else:
                t+=1
                print('У терроров ' + str(t) + ' очков!')
            continue
        else:
            print('Тебе нанесли ' + str(nanesli) + ' урона, твои хп  ' + str(hpchela))
    rask = random.choice(raskidka)
    if rask == 'Нанесли урон ':
        hpchela -= random.randint(1, hpchela)
        if hpchela <= 0:
            time.sleep(1.5)
            print(Back.BLACK+Fore.RED+'Тебя'+Fore.LIGHTRED_EX+' убили'+Fore.RED+' раскидкой')
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
            pok=''
            inventory.clear()

            if vib == 't':
                ct+=1
                print('У контр-терроров '+str(ct)+' очков!')
            else:
                t+=1
                print('У терроров ' + str(t) + ' очков!')
            continue
        else:
            time.sleep(1.5)
            print('По тебе попали раскидкой, твои хп - ' + str(hpchela))
    else:
        time.sleep(1.5)
        print('Тебе повезло по тебе не попали раскидкой!')
    if chel == 'Попадание':
        chel1=random.choice(chel_hp)
        if chel1 == 'Тот ':
            print('Это тот чувак , у него '+str(hp_vraga)+' хп')
            time.sleep(2)
            print('Выстрел')
            pop=random.choice(p50)
            if pop == 'Попал' and gun[vib][pok]['damage']>= hp_vraga:
                print('Ты убил врага')
            elif pop == 'Попал' and gun[vib][pok]['damage']< hp_vraga:
                print('ты попал, у него '+str(hp_vraga-gun[vib][pok]['damage'])+' хп')
            else:
                nanesli=random.randint(1,hpchela)
                print('тебе нанесли '+str(hpchela-nanesli)+' урона')
                print(Back.BLACK + Fore.RED + 'Тебя ' + Fore.LIGHTRED_EX + 'убили ')
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
                continue
    else:
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
            hp_vraga = 100 - gun[vib][pok]['damage']
            chel = 'Попадание'
        else:
            print('Не попал')
            nanesli = random.randint(1, 100)
            hpchela -= nanesli
            if hpchela <= 0:
                time.sleep(1.5)
                print(Back.BLACK + Fore.RED + 'Тебя ' + Fore.LIGHTRED_EX + 'убили ')
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
                continue
    bal+=3200
    print(bal)
    if vib == 't':
        ct += 1
        print('У контр-терроров ' + str(ct) + ' очков!')
    else:
        t += 1
        print('У терроров ' + str(t) + ' очков!')
    continue












                        # urn=input('Завершить игру?:\n')
                        # if urn == 'да':
                        #     exit()
