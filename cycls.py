x = input ()
t = 0
o =0
u = 0
for i in x:
    u +=1
    if i == '1':
        print('вводить 1 нельзя')
        o+=1
        continue
    t += 1
    print(i)
print('-'*10)
print(u)
print('-'*10)
print(t)
print('-'*10)
print(o)
print('программа идет дальше')
