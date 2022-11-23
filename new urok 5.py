from random import randint
def spisok(*args, k=False):
    new_list = []
    for i in args:
        for y in i:
            if int(y) not in new_list:
                new_list.append((int(y)))
    if k == True:
        new_list.sort()
    return new_list


z = list(input('Первый лист:\n').split(','))
x = list(input("Второй лист:\n").split(','))
c = list(input('Третий лист:\n').split(','))
k=randint(1,2)
print(k)
if k == 1:
    print( spisok(z, x, c,k=True))
else:
    print(spisok(z, x, c, k=False))
