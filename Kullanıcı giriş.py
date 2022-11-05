print("""******************
KULLANICI GİRİŞİ
******************""")
SYS_KULLANICI_ADI="Kondansatör Agah"
SYS_KULLANICI_SIFRE="11111111"
Giriş_hakkı=3
while True:
    ka=input("Kullanıcı adını girin:")
    ks=input("Kullanıcı şifresini girin")
    if(SYS_KULLANICI_ADI==ka and SYS_KULLANICI_SIFRE==ks):
        print("Başarıyla sisteme giriş yaptınız...")
    elif(SYS_KULLANICI_ADI!=ka and SYS_KULLANICI_SIFRE==ks):
        print("Kullanıcı adı yanlış girildi...")
        Giriş_hakkı-=1
    elif(SYS_KULLANICI_ADI==ka and SYS_KULLANICI_SIFRE!=ks):
        print("Şifre yanlış girildi...")
        Giriş_hakkı-=1
    elif(SYS_KULLANICI_ADI!=ka and SYS_KULLANICI_SIFRE!=ks):
        print("Bilgiler yanlış girildi...")
        Giriş_hakkı-=1
    else:
        print("Hatalı giriş denemesi")
        break
    if(Giriş_hakkı==0):
        print("giriş hakkı kalmadı")
        break
        
