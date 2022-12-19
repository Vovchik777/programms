from pprint import pprint

x = input ()
for i in x:
    if i == '1':
        print('вводить 1 нельзя')
        continue
    print(i)
print('программа идет дальше')
pprint("1 "
       "2 "
       "3 "
       "4 "
       "5")