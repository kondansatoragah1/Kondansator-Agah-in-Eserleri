oyun=[["0|","-","-","-"],
      ["1|","-","-","-"],
      ["2|","-","-","-"]]
def show():
    print("   0 1 2")
    print("---------")
    for a in oyun:
        for b in a:
            print(b,end=" ")
        print()
def player1(a,b,l):
    if l[a][b+1]=="-":                                                  
        l[a][b+1]="X"                                                  
    else:
        print("That position already taken...")
def player2(a,b,l):
    if l[a][b+1]=="-":
        l[a][b+1]="O"
    else:
        print("That position already taken...")

def kontrol_etme1(a):
    
    
    if ((a[0][1]==a[0][2]) and (a[0][1]==a[0][3])) and a[0][1]=="X":
        print("Player 1 Wins")
        return True
    
    
    if ((a[1][1]==a[1][2]) and (a[1][1]==a[1][3])) and a[1][1]=="X":
        print("Player 1 Wins")
        return True
    if ((a[2][1]==a[2][2]) and (a[2][1]==a[2][3])) and a[2][1]=="X":
        print("Player 1 Wins")
        return True
    if ((a[0][1]==a[1][1]) and (a[0][1]==a[2][1])) and a[0][1]=="X":
        print("Player 1 Wins")
        return True
    if ((a[0][2]==a[1][2]) and (a[0][2]==a[2][2])) and a[0][2]=="X":
        print("Player 1 Wins")
        return True
    if ((a[0][3]==a[1][3]) and (a[0][3]==a[2][3])) and a[0][3]=="X":
        print("Player 1 Wins")
        return True
    if ((a[0][1]==a[1][2]) and (a[0][1]==a[2][3])) and a[0][1]=="X":
        print("Player 1 Wins")
        return True
    if ((a[0][3]==a[1][2]) and (a[0][3]==a[2][1])) and a[0][3]=="X":
        print("Player 1 Wins")
        return True
def kontrol_etme2(a):
    if ((a[0][1]==a[0][2]) and (a[0][1]==a[0][3])) and a[0][1]=="X":
        print("Player 2 Wins")
        return True
    if ((a[1][1]==a[1][2]) and (a[1][1]==a[1][3])) and a[1][1]=="O":
        print("Player 2 Wins")
        return True
    if ((a[2][1]==a[2][2]) and (a[2][1]==a[2][3])) and a[2][1]=="O":
        print("Player 2 Wins")
        return True
    if ((a[0][1]==a[1][1]) and (a[0][1]==a[2][1])) and a[0][1]=="O":
        print("Player 2 Wins")
        return True
    if ((a[0][2]==a[1][2]) and (a[0][2]==a[2][2])) and a[0][2]=="O":
        print("Player 2 Wins")
        return True
    if ((a[0][3]==a[1][3]) and (a[0][3]==a[2][3])) and a[0][3]=="O":
        print("Player 2 Wins")
        return True

    if ((a[0][1]==a[1][2]) and (a[0][1]==a[2][3])) and a[0][1]=="O":
        print("Player 2 Wins")
        return True
    if ((a[0][3]==a[1][2]) and (a[0][3]==a[2][1])) and a[0][3]=="O":
        print("Player 2 Wins")
        return True
hamle = 0        
print("**********THE TIC TAC TOE GAME**********")
print()
print()
while True:
    
    show()
    print()
    o1x=int(input("Player 1 - Please enter a row number "))
    print()
    o1y=int(input("Player 1 - Please enter a column number "))
    print()
    player1(o1x,o1y,oyun)
    x=kontrol_etme1(oyun)
    if x==True:
        break
    hamle+=1
    if hamle==9:
        print("The conditions are draw")
        print("GAME OVER")
        break
    show()
    print()
    o2x=int(input("Player 2 - Please enter a row number "))
    print()
    o2y=int(input("Player 2 - Please enter a column number "))
    print()
    player2(o2x,o2y,oyun)
    y=kontrol_etme2(oyun)
    if y==True:
        break
    hamle+=1
    
            
    
    
    
    
    
    
