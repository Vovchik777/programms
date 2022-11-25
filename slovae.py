abc={'a':1,'b':2,'c':3}
new={}
for key, value in abc.items():
    new[value]=key
    print(new)
for i in abc:
    abc[i]=abc[i]*round(0.85,2)
print(abc)
for value in abc.values():
    print(value)