from random import randint
while True:
    chel = 0
    komp = 0
    o = int(input("До скольки очкков играем???:\n"))
    while True:
        #while chel < o or komp < o:
        a = input('Камень = 1 Ножницы ✂️ = 2 Бумага = 3 Выбери:\n')
        if int(a) >= 4:
            print('Такого варианта нету!!!')
            break
        b = randint(1, 3)
        print(b)
        if a == '0':
            print('Конец игры')
            continue
        if a == '1' and str(b) == '2':
            chel += 1
        elif a == '2' and str(b) == '1':
            komp += 1
        elif a == '3' and str(b) == '1':
            chel += 1
        elif a == '1' and str(b) == '3':
            komp += 1
        elif a == str(b):
            print('Ничья')
        elif a == '2' and str(b) == '3':
            chel += 1
        elif a == '3' and str(b) == '2':
            komp += 1
        print(' у компа ' + str(komp) + " У тебя " + str(chel))
        if chel == o or komp == o:
            if chel < komp:
                print('Комп победил')
            elif chel > komp:
                print('Ты победил')
            break
