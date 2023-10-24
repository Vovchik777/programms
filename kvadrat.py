# A = int(input("\nразмер крыши:\n"))
# A = A * 2 - 1
# c = A
# d = 0
# while d < A:
#     print(' ' * (A - 1) + ' ' * d + '*')
#     d += 1

# while True:
#     a = int(input("\nразмер квадратa:\n"))
#     if a <= 1:
#         print('введите число побольше')
#     else:
#         rk=a*2-1
#         print(' '*int(rk/2)+'*')
#         for i  in range(2,a):# ,2):
#             print( ' '*(rk-i-a)+ "*" ' '*i+ '*')
#         print('* ' * a)
#         b = a - 2
#         for i in range(b):
#             print('* ', end='')
#             print(' ' * 2 * b + '*')
#         for i in range(a):
#             print('* ', end='')
a = int(input("\nразмер квадратa:\n"))
if a <= 1:
    print('введите число побольше')
else:
    rk=a*2-1
    print(' '*int(rk/2)+'*')
    for i  in range(2,a):# ,2):
        print( ' '*(rk-i-a)+ "*" ' '*i+ '*')
    print('* ' * a)
    b = a - 2
    for i in range(b):
        print('* ', end='')
        print(' ' * 2 * b + '*')
    for i in range(a):
        print('* ', end='')
