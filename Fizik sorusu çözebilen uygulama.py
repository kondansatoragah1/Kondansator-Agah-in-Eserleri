# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:35:44 2022

@author: Acer
"""
print("""         _______________
         |____|         |  Soldaki cisim , sağdaki cisim arasında sürtünmeli zemin var
              |_________|  ve uygulanan kuvvetler soldaki cismi sabit tutabilir mi sorusuna yanıt veren program.... :d
              
         
            """)
              





m1=int(input("soldaki cismin kütlesi"))
m2=int(input("sağdaki cismin kütlesi"))
m1g=m1*10
m2g=m2*10
solk=int(input("sol kuvvet"))
sağk=int(input("sağ kuvvet"))
fsks=float(input("sürtünme katsayısını gir"))
fnet=solk-sağk
mtop=m1+m2
asis=fnet+mtop
if solk>sağk:
    f1=asis*m1-solk
    fs=f1*fsks
    
    if m1g>fs:
        fs=m1g
        fskso=fs/f1
        print("Cisim yerinde durmayacaktır...","Durması için sürtünme katsayısı",fskso,"olmalıdır.")
    else:
        print("Cisim durabilecektir...")
elif sağk>solk:
    f1=asis*m1+solk
    fs=f1*fsks
    if m1g>fs:
        fs=m1g
        fskso=fs/f1
        print("Cisim yerinde durmayacaktır...","Durması için sürtünme katsayısı",fskso,"olmalıdır.")
        
    else:
        print("Cisim durabilecektir...")