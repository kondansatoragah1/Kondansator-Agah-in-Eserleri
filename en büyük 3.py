
a=0
while True:
    değer1=0
    değer2=0
    değer3=0
    
    a=int(input("sayı gir"))
    
    if a>=değer1:
        değer1=a
        continue
    elif a>=değer2:
        değer2=a
        continue
    elif a>=değer3:
        değer3=a
        continue
    else:
        break
    if a==-1:
        liste=[]
        liste.append(değer1)
        liste.append(değer2)
        liste.append(değer3)
        liste.sort()
        print(liste[-1],liste[-2],liste[-3])
    
