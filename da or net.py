# a=0
# b=[]
# while a <= 999:
#     a=int(input('Введите число:\n'))
#     b.append(a)
# print(min(b)
minimum=''
while True:
    vvod=int(input('Введи число:\n'))
    if minimum=='' or vvod < minimum:
        minimum=vvod
    if vvod>999:
        break

print(minimum)