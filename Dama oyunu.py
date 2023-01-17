liste=[
       ["X" for x in range(6)],
       ["X" for x in range(6)],
       ["-" for x in range(6)],
       ["-" for x in range(6)],
       ["-" for x in range(6)],
       ["-" for x in range(6)],
       ["-" for x in range(6)],
       ["O" for x in range(6)],
       ["O" for x in range(6)],
       ]

def show():
    print("  ",end="")
    for a in range(0,6):
       
        print(a,sep="",end="  | ")
    print()
    for a in range(0,9):
        print(a,end="")
        print(liste[a])



def movement_1(a,raw,column,raw1,column1):
    if (raw+1==raw1 and column+1==column1) or (raw+1==raw1 and column-1==column1) or (raw1-raw>2 or column1-column>2) or (a[raw1][column1]=="X") or ((raw1>8 or column1>5) or (raw1<0 or column1<0)):
        print("This process is not allowed order exchanged....")
        return "a"
    if a[raw][column]=="X" :
        a[raw1][column1],a[raw][column]=a[raw][column],a[raw1][column1]
        
    else:
        print("This position already taken...")
    
def movement_2(a,raw,column,raw1,column1): 
    if (raw-1==raw1 and column+1==column1) or (raw-1==raw1 and column-1==column1) or (raw-raw1>2 or column-column1>2) or (a[raw1][column1]=="O") or ((raw1>8 or column1>5) or (raw1<0 or column1<0)):
        print("This process is not allowed order exchanged....")
        return "a"      
    if a[raw][column]=="O" :
        a[raw1][column1],a[raw][column]=a[raw][column],a[raw1][column1]
        
    else:
        print("This position already taken...")


def check(a):
    for column in range(4):
        for raw in range(5):
            if ((a[raw][column]=="X" and a[raw+2][column]=="X") and a[raw+1][column]=="O"):
                a[raw+1][column]="-"
            if ((a[raw][column]=="O" and a[raw+2][column]=="O") and a[raw+1][column]=="X"):
                a[raw+1][column]="-"
    for raw in range(5):
        for column in range(4):
            if ((a[raw][column]=="X" and a[raw][column+2]=="X") and a[raw][column+1]=="O"):
                a[raw][column+1]="-"
            if ((a[raw][column]=="O" and a[raw][column+2]=="O") and a[raw][column+1]=="X"):
                a[raw][column+1]="-"
def system_check(a):
    if a.count("X")>a.count("O"):
        return True
    else:
        print("Player_2 Won")
        return False
hamle=0
show()

while hamle<20:
    print()
    x=int(input("Please enter a raw for player-1:"))
    y=int(input("Please enter a column for player-1:"))
    z=int(input("To where?:"))
    k=int(input("To where?:"))
    movement_1(liste, x, y,z,k)
    check(liste)
    show()
    hamle+=1
    x=int(input("Please enter a raw for player-2:"))
    y=int(input("Please enter a column for player-2:"))
    z=int(input("To where?:"))
    k=int(input("To where?:"))
    movement_2(liste, x, y,z,k)
    check(liste)
    show()
    hamle+=1
    
    
    
    
    
    

    




    
    

    
    
    
        