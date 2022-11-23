summa=0
a=[]
while True:
    c=input('Число, надоело-пиши vse')
    t=c.replace('-','') .isdigit()
    if t :
        a.append(int(c))
    elif c == 'vse':
        print(a)
        for i in range(2,len(a),3):
            summa+=a[i]
        print(summa)
        break







