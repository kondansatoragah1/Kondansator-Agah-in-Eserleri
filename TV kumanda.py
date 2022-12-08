liste=["Kanal1", "Kanal2", "Kanal3"]
sesdurumu=0
kanaldurumu="Kanal1"
tvdurum="Kapalı"


def ses(x):
    global sesdurumu,yzt
    if x<0:
        sesdurumu-=x
        
        return sesdurumu
        
    elif x>0:
        sesdurumu+=x
        return sesdurumu
def kanal(a):
    
    global kanaldurumu,liste
    
    if a=="q":
        print("Fonksiyondan çıkıldı")
        return kanaldurumu
    
    elif a==1:
        
        kanaldurumu=liste.index[0]
        return kanaldurumu
    elif a==2:
        
        kanaldurumu=liste.index[1]
        return kanaldurumu
    elif a==3:
        
        kanaldurumu=liste.index[2]
        return kanaldurumu

def tvdurumu(x):
    global tvdurum
    if x==0:
        if tvdurum=="Kapalı":
            print("Televizyon zaten kapalı...")
            
        else:
            tvdurum="Kapalı"
            print("Televizyon",tvdurum)
            return tvdurum
    elif x==1:
        if tvdurum=="Açık":
            print("Televizyon zaten açık...")
            
        else:
            tvdurum="Açık"
            print("Televizyon",tvdurum)
            return tvdurum
    
while True:
    x=input("Hangi fonksiyonu istersiniz....")
    if x=="Kanal":
        print("""Kanal Listesi:
            1.Kanal 1
            2.Kanal 2
            3.Kanal 3
            çıkış için "q" ya basın""")
        y=int(input("Sayıyı girin..."))
        kanal(y)
        print("Şuanki kanal:",kanaldurumu)
        continue
    elif x=="Ses":
        y=int(input("Ne kadar artırmak veya azaltmak istediğinizi girin...(+3,-2 vb...)"))
        ses(y)
        print("Şuanki ses durumu:",sesdurumu)
        continue
    elif x=="TV":
        z=int(input("""   Kapatmak için 0'i\nAçmak için 1 yaz..."""))
        tvdurumu(z)
        print("Şuanki tv durumu:", tvdurum)
        continue
        
    
        
    
        

    
    
