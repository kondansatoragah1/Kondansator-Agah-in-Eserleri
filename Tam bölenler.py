
liste=[]
def tambölen(x):
    for i in range(1,x+1):
        if x%i==0:
            liste.append(i)
while True:
    x=int(input("Sayı gir"))
    tambölen(x)
    print("Tamb bölenleri:",liste)
    liste.clear()
    continue
            
    
