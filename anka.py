import math
n = int(input('Сколько чисел вводим?:\n'))
a = int(input('Введите число :\n'))
min = a

for i in range(0,n-1):
    a = int(input('Введите число :\n'))
    if min > a:
        min = a

print(min)
print(math.sqrt(min))
