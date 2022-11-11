def karesığdırmaca(x,y,z,t):
    u=x+y
    if u<=z:
        print("Sığar")
    elif u<=t:
        print("Sığar")
    else:
        print("Sığmaz")
while True:
    x=int(input("1.Karenin kenarını gir"))
    y=int(input("2.Karenin kenarını gir"))
    z=int(input("Dikdörtgenin 1.kenarını gir"))
    t=int(input("Dikdörtgenin 2.kenarını gir"))
    karesığdırmaca(x,y,z,t)
    continue
    
