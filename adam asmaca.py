words=["man","bent"]
def show(a):
    if a==0:
        print(temp)
        print("|",end=" ")
        for b in range(4):
            print("-",end=" ")
        print()
        for b in range(6):
            print("|")
    elif a==1:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        for a in range(5):
            print("|")
    elif a==2:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        for a in range(4):
            print("|")
    elif a==3:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        for a in range(3):
            print("|")
    elif a==4:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        print("|     |")
        for a in range(2):
            print("|")
    elif a==5:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        print("|     |")
        print("|     |")
        for a in range(1):
            print("|")
    elif a==6:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        print("|    /|")
        print("|     |")
        for a in range(1):
            print("|")
    elif a==7:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        print("|    /|\ ")
        print("|     |")
        for a in range(1):
            print("|")
    elif a==8:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        print("|    /|\ ")
        print("|     |")
        print("|    / ")    
        for a in range(0):
            print("|")
    elif a==9:
        print(temp)
        print("|",end=" ")
        for a in range(4):
            print("-",end=" ")
        print()
        print("|     |")
        print("|     |")
        print("|     O")
        print("|    /|\ ")
        print("|     |")
        print("|    / \ ")    
        for a in range(0):
            print("|")
def check(a,b):
    i=0
    for x in a:
        if x==b:
            temp[i]=b
            return True
        else:
            i+=1
    return False 
point=0
wrong=0
n=0
while n<2:
    for a in words:
        the_true=[]
        wrong=0
        temp=[]
        for i in a:
            temp.append("_")
        the_true=[x for x in a]
        n+=1
        while True:
            if temp==the_true:
                print(temp)
                point+=1
                print("Your total point are ",point)
                print("You won")
                break
            show(wrong)
            x=input("Please enter a character: ")
            z=check(the_true,x)
            if z==False:
                wrong+=1
            else:
                continue
            if wrong==9:
                show(wrong)
                print(temp)
                point-=1
                print("Your total point are ",point)
                print("You lost")
                break
    
            
        
    
        
