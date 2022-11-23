# #a = input('Строка:\n')
# s = 0
# for i in input('Строка:\n'):
#     s+=int(i)
# print(s)
#
while True:
    ch=int(input('\n''Введи число:\n'))
    if ch <= 0:
        print('Вводить  меньше 0 нельзя!!')
        break
    s = ''
    while ch > 0:
        ch-=1
        s+='*'
    print(s)
#     print('*',end='')
#     ch-=1
