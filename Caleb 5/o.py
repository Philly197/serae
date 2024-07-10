def grid(n):
    for i in range(0, len(n)):
        print(n[i])
    
me="&"

x=1
y=1

gridie=[
    ["#","#","#","#","#","#","#","#","#","#","#"],
    ["#",me,"-","-","*","-","-","-","-","-","#"],
    ["#","-","-","-","-","-","-","b","-","-","#"],
    ["#","#","#","-","-","-","-","-","-","*","#"],
    ["#","#","-","-","-","-","*","-","b","-","#"],
    ["#","#","#","-","-","h","-","-","-","-","#"],
    ["#","#","-","-","-","-","-","-","-","-","#"],
    ["#","-","-","-","*","-","-","-","-","-","#"],
    ["#","#","-","-","-","-","-","-","-","-","#"],
    ["#","#","#","#","#","#","#","#","#","#","#"]
]

score=0
win=False
while win == False:
    grid(gridie)

    z=input("Use WASD: ")
    gridie[x][y] = "-"
    if z == "w" and gridie[x-1][y] =="#":
        print('You cant move there!')
    elif z == "w" and gridie[x-1][y] == "b" and gridie[x-2][y] == "-":
        x-=1
        gridie[x][y]="me"
        gridie[x-1][y]="b"
        gridie[x+1][y]="-"
    elif z == "w" and gridie[x-1][y]=="-":
        x-=1
        gridie[x][y]="me"
        gridie[x+1][y]="-"
    elif z == "w" and gridie[x-1][y] == "b" and gridie[x-2][y] == "*":
        score+=1
        x-=1
        gridie[x][y]="me"
        gridie[x-1][y]="b"
    elif z == "w" and gridie[x-1][y] == "h":
        x-=1
        gridie[x][y]="me"
        gridie[x+1][y]="-"
        win=True
        print("You lost the game, you fell into the black hole.")
    
    elif z == "a" and gridie[x][y-1] =="#":
        print('You cant move there!')
    elif z == "a" and gridie[x][y-1] == "b" and gridie[x][y-2] == "-":
        y-=1
        gridie[x][y]="me"
        gridie[x][y-1]="b"
        gridie[x][y+1]="-"
    elif z == "a" and gridie[x][y-1] == "-":
        y-=1
        gridie[x][y]="me"
        gridie[x][y+1]="-"
    elif z == "a" and gridie[x][y-1] == "b" and gridie[x][y-2] == "*":
        score+=1
        y-=1
        gridie[x][y]="me"
        gridie[x][y-1]="b"
    elif z == "a" and gridie[x][y-1] == "h":
        y-=1
        gridie[x][y]="me"
        gridie[x][y+1]="-"
        win=True
        print("You lost the game, you fell into the black hole.")
    
    elif z == "s" and gridie[x+1][y] =="#":
        print('You cant move there!')
    elif z == "s" and gridie[x+1][y] == "b" and gridie[x+2][y] == "-":
        x+=1
        gridie[x][y]="me"
        gridie[x+1][y]="b"
        gridie[x-1][y]='-'
    elif z == "s" and gridie[x+1][y] == "-":
        x+=1
        gridie[x][y]="me"
        gridie[x-1][y]="-"
    elif z == "s" and gridie[x+1][y] == "b" and gridie[x+2][y] == "*":
        score+=1
        x+=1
        gridie[x][y]="me"
        gridie[x+1][y]="b"
    elif z == "s" and gridie[x+1][y] == "h":
        x+=1
        gridie[x][y]="me"
        gridie[x-1][y]="-"
        win=True
        print("You lost the game, you fell into the black hole.")
    
    elif z == "d" and gridie[x][y+1] =="#":
       print('You cant move there!')
    elif z == "d" and gridie[x][y+1] == "b" and gridie[x][y+2] == "-":
        y+=1
        gridie[x][y]="me"
        gridie[x][y+1]="b"
        gridie[x][y-1]='-'
    elif z == "d" and gridie[x][y+1] == "-":
        y+=1
        gridie[x][y]="me"
        gridie[x][y-1]="-"
    elif z == "d" and gridie[x][y+1] == "b" and gridie[x][y+2] == "*":
        score+=1
        y+=1
        gridie[x][y]="me"
        gridie[x][y+1]="b"
    elif z == "d" and gridie[x][y+1] == "h":
        y+=1
        gridie[x][y]="me"
        gridie[x][y-1]="-"
        win=True
        print("You lost the game, you fell into the black hole.")

    if score == 3:
        win=True
        print('You have won the game!')
   
    print(score)
    
        


