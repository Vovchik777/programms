from colorama import init, Fore
from colorama import Style

COLOR_X = Fore.RED
COLOR_0 = Fore.BLUE


def get_player_color(pole):
    if pole == 'X':
        return COLOR_X
    elif pole == '0':
        return COLOR_0
    else:
        return ''


def show_pole():
    print(
        f' {get_player_color(pole[0]) + pole[0] + Style.RESET_ALL} │ {get_player_color(pole[1]) + pole[1] + Style.RESET_ALL} │ {get_player_color(pole[2]) + pole[2] + Style.RESET_ALL} \n'
        f'───┼───┼───\n'
        f' {get_player_color(pole[3]) + pole[3] + Style.RESET_ALL} │ {get_player_color(pole[4]) + pole[4] + Style.RESET_ALL} │ {get_player_color(pole[5]) + pole[5] + Style.RESET_ALL} \n'
        f'───┼───┼───\n'
        f' {get_player_color(pole[6]) + pole[6] + Style.RESET_ALL} │ {get_player_color(pole[7]) + pole[7] + Style.RESET_ALL} │ {get_player_color(pole[8]) + pole[8] + Style.RESET_ALL} \n'

    )


init(autoreset=False)
count = 0
pole = [Fore.LIGHTBLACK_EX + '0', Fore.LIGHTBLACK_EX + '1', Fore.LIGHTBLACK_EX + '2', Fore.LIGHTBLACK_EX + '3',
        Fore.LIGHTBLACK_EX + '4', Fore.LIGHTBLACK_EX + '5', Fore.LIGHTBLACK_EX + '6', Fore.LIGHTBLACK_EX + '7',
        Fore.LIGHTBLACK_EX + '8' + Style.RESET_ALL]
name_x = input('Кто играет за X:\n')
name_0 = input('Кто играет за 0:\n')
gameover = False
playertek = "X"

show_pole()

while not gameover:
    try:
        if playertek == 'X':
            nomerkletki = int(input(f'Ходит {COLOR_X + name_x + Style.RESET_ALL} номер клетки:'))
        else:
            nomerkletki = int(input(f'Ходит {COLOR_0 + name_0 + Style.RESET_ALL} номер клетки:'))
    except ValueError:
        print('Это не число!!')
        continue
    if nomerkletki >= 0 and nomerkletki <= 8:
        if pole[nomerkletki] not in ['0', 'X']:
            pole[nomerkletki] = playertek
            count += 1
            show_pole()
            if playertek == 'X':
                playertek = '0'
            else:
                playertek = "X"
        else:
            print('Эта клетка занята')
            continue
    else:
        print('такой клетки нету')
        continue

    if pole[0] == pole[1] == pole[2] == '0' or \
            pole[3] == pole[4] == pole[5] == '0' or \
            pole[6] == pole[7] == pole[8] == '0' or \
            pole[0] == pole[3] == pole[6] == '0' or \
            pole[1] == pole[4] == pole[7] == '0' or \
            pole[2] == pole[5] == pole[8] == '0' or \
            pole[0] == pole[4] == pole[8] == '0' or \
            pole[2] == pole[4] == pole[6] == '0':
        print(f'Победил {COLOR_0 + name_0+Style.RESET_ALL} ')
        gameover = True
    elif pole[0] == pole[1] == pole[2] == 'X' or \
            pole[3] == pole[4] == pole[5] == 'X' or \
            pole[6] == pole[7] == pole[8] == 'X' or \
            pole[0] == pole[3] == pole[6] == 'X' or \
            pole[1] == pole[4] == pole[7] == 'X' or \
            pole[2] == pole[5] == pole[8] == 'X' or \
            pole[0] == pole[4] == pole[8] == 'X' or \
            pole[2] == pole[4] == pole[6] == 'X':
        print(f'Победил {COLOR_X + name_x+Style.RESET_ALL} ')
        gameover = True
    else:
        if count == 9:
            print('Ничья')
            gameover = True
input("Нажмите Enter для выхода")
