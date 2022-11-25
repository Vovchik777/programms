from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=False)
count = 0
pole = [Fore.LIGHTBLACK_EX + '0', Fore.LIGHTBLACK_EX + '1', Fore.LIGHTBLACK_EX + '2', Fore.LIGHTBLACK_EX + '3',
        Fore.LIGHTBLACK_EX + '4', Fore.LIGHTBLACK_EX + '5', Fore.LIGHTBLACK_EX + '6', Fore.LIGHTBLACK_EX + '7',
        Fore.LIGHTBLACK_EX + '8']
name0=input('Кто играет за 0:\n')
namex=input('Кто играет за X:\n')
gameover = False
playertek = "X"
print(f' {pole[0]} │ {pole[1]} │ {pole[2]} \n'
      f'───┼───┼───\n'
      f' {pole[3]} │ {pole[4]} │ {pole[5]} \n'
      f'───┼───┼───\n'
      f' {pole[6]} │ {pole[7]} │ {pole[8]} \n'
      )
while not gameover:
    if playertek == 'X':
        nomerkletki = int(input(f'Ходит {namex} номер клетки:'))
    else:
        nomerkletki = int(input(f'Ходит {name0} номер клетки:'))
    if pole[nomerkletki] not in ['0', 'X']:
        pole[nomerkletki] = playertek
        count += 1
        print(f' {pole[0]+Style.RESET_ALL} │ {pole[1]+Style.RESET_ALL} │ {pole[2]+Style.RESET_ALL} \n'
              f'───┼───┼───\n'
              f' {pole[3]+Style.RESET_ALL} │ {pole[4]+Style.RESET_ALL} │ {pole[5]+Style.RESET_ALL} \n'
              f'───┼───┼───\n'
              f' {pole[6]+Style.RESET_ALL} │ {pole[7]+Style.RESET_ALL} │ {pole[8]+Style.RESET_ALL} \n'
              )
    else:
        print('Эта клетка занята')
        continue

    if pole[0] == pole[1] == pole[2] == 'O'  or \
            pole[3] == pole[4] == pole[5] == 'O' or \
            pole[6] == pole[7] == pole[8] == 'O' or \
            pole[0] == pole[3] == pole[6] == 'O'  or \
            pole[1] == pole[4] == pole[7] == 'O'  or \
            pole[2] == pole[5] == pole[8] == 'O' or \
            pole[0] == pole[4] == pole[8] =='O'  or \
            pole[2] == pole[4] == pole[6] == 'O':
        print(f'Победил {name0} ')
    elif pole[0] == pole[1] == pole[2] == 'X'  or \
            pole[3] == pole[4] == pole[5] == 'X' or \
            pole[6] == pole[7] == pole[8] == 'X' or \
            pole[0] == pole[3] == pole[6] == 'X'  or \
            pole[1] == pole[4] == pole[7] == 'X'  or \
            pole[2] == pole[5] == pole[8] == 'X' or \
            pole[0] == pole[4] == pole[8] =='X'  or \
            pole[2] == pole[4] == pole[6] == 'X':
        print(f'Победил {namex} ')
        gameover = True
    else:
        if count == 9:
            print('Ничья')
    if playertek == 'X':
        playertek = 'O'
    else:
        playertek = "X"
# print(' '+X +' │ '+O+' │ ' +X+'  \n'+'───┼───┼───\n'+'\n')
# print('│┼─')
#  X │ X │ X
# ───┼───┼───
#  X │ X │ X
# ───┼───┼───
#  X │ X │ X
