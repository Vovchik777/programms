a = input('ЧИсла или строки')
b = list(a)
print('Английских ' + str(b.count('a')))
print('Руccких ' + str(b.count('а')))
print('Английских больших ' + str(b.count('A')))
print('Руccких больших ' + str(b.count('А')))
# while True:
#     a=(input('Числа или строки:\n'))
#     a=list(a)
#     print((list(reversed(a))))
# import a as a
#
# a = int(input())
# print("The next number for the number ",str(a+1)," is "+str(a-1)+'.')
# print("The previous number for the number "+str(a)+" is "+str(a)+'.')