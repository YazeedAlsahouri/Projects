"""
This code for Tic Tac Toe Game!!
"""
import random
def O_check(winO):
    O_keys=[]
    for j in winO.keys():
        O_keys.append(int(j))
    if len(O_keys)>=3:
        flag=False
        Win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        s=0
        for i in Win:
            s=0
            q=sum(i)
            for k in O_keys:
                if k in i:
                   s+=k         
            if q==s:
                flag=True
        return flag      
def X_check(winX):
    X_keys=[]
    for j in winX.keys():
        X_keys.append(int(j))
    if len(X_keys)>=3:
        flag=False
        Win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        s=0
        for i in Win:
            s=0
            q=sum(i)
            for k in X_keys:
                if k in i:
                   s+=k 
            if q==s:
                flag=True
        return flag     
choice=input("Do you want to play Tic Tac Toe Game?(Yes/No): ").capitalize()
if choice=="Yes":
    c=1
    pattern_game=""
    pattern_play=""
    for i in range(3):
        for j in range(3):
            print(f"| {c} ",end="")
            pattern_game+=f"| {c} "
            pattern_play+=f"| {c} "
            c+=1
        print("|")
        pattern_game+="|\n"
        pattern_play+="|\n"
        numbers=["1","2","3","4","5","6","7","8","9"]
        winX={}
        winO={}
    while numbers!=[]:
        player_X_turn=input("X's turn Enter a position: ")
        while not player_X_turn in numbers:
              player_X_turn=input("Postion is marked Try again:")  
        numbers.remove(player_X_turn)
        winX[player_X_turn]="X"
        pattern_play=pattern_play.replace(player_X_turn, "X")
        pattern_game=pattern_play
        for i in range(len(pattern_game)):
            if pattern_game[i].isdigit():
                pattern_game=pattern_game.replace(pattern_game[i], " ")
        print(pattern_game)
        if numbers==[]:
            break
        player_O_turn=random.choice(numbers)
        while not player_O_turn in numbers:
            player_O_turn=random.choice(numbers)
        numbers.remove(player_O_turn)
        print(f"O's Choose {player_O_turn}")
        winO[player_O_turn]="O"
        pattern_play=pattern_play.replace(player_O_turn, "O")
        pattern_game=pattern_play
        for i in range(len(pattern_game)):
            if pattern_game[i].isdigit():
                pattern_game=pattern_game.replace(pattern_game[i], " ")
        print(f"\n{pattern_game}")
        x=X_check(winX)
        o=O_check(winO)
        if numbers==[]:
            break
        if x:
            print("Player (X) Wins Congratulation!!")
            break
        elif o:
            print("Player (O) Wins Congratulation!!")
            break
        if numbers==[]:
            break
    if not x and not o:
        print("Draw!!!")
elif choose=="No":
    print("Thank You!!")
else:
    raise Exception("ErrorValueInput")
