P=input("Parol?")
if P=="Programma123":
    print("Parol vernii")
    d=float(input("Dengi?") )
    p=float(input("Prozent?"))
    n=float(input("Vremya?"))
    s=d*(1+0.01*p)**n
    print(str(s))
else :
    print("Parol ne vernii")