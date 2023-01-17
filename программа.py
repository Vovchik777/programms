a = input("Chto delaem : +, - , / , * ,% -chs, pi, okr, okr1,**1,**2")
if a == "pi":
    import math
    print("uchi mateshu chiclo pi rovno "+str(math.pi))
else:
    b = float ( input ("Vvedi pervoe chislo:") )
    c = float ( input ("Vvedi vtoroe chislo :") )
    if a == "-" :
        print("Otvet " +str(b - c)+ " ura")
    elif a == "+" :
        print("Otvet " +str(b + c)+ " ura")
    elif a == "/" :
        if c == 0:
            print("Na nol delit nelzya")
        else :
            print("Otvet " +str(b / c)+ " ura")
    elif a == "*" :
        print("Otvet " +str(b * c)+ " ura")
    elif a == "%" :
        print("Otvet " +str(b % c)+ " ura!!!")
    elif a == "-chs":
        print("Otvet"+ str(-b) +"i"+ str(-c)+"a ti, loh ne poshital")
    elif a =="okr":
        import math
        print("otvet", math.floor(b),math.floor(c),)
    elif a =="okr1":
        import math
        print("otvet", math.ceil(b), math.ceil(c),)
    elif a=="**1":
        print("otvet "+str(b**c)+" vce")
    elif a=="**2":
        print("otvet "+str(c**b)+" vce")
    else :
        print("Neponatnaya komanda")