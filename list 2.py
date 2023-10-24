n = int(input())
r = 0
for i in range (0,n):
    c = 11**i
    print(c)
    r+=1
    print('-'*1000)
    print(r)
    print('-' * 1000)
c1 = list(str(c))
print(len(c1))