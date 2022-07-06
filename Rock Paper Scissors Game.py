import random
choice=input("Do you want to play Rock Paper Scissors?(Yes/No): ").capitalize()
if choice=="Yes":
    game_list=["Rock","Paper","Scissors"]
    count_play=int(input("How Many times you want to play? "))
    count_win=0
    for i in range(count_play):
        computer_choice=random.choice(game_list)
        player_choice=input("Enter your choice: ").capitalize()
        print(f"{computer_choice} VS {player_choice}")
        if computer_choice=="Rock" and player_choice=="Rock":
            print("Draw!!")
        elif computer_choice=="Rock" and player_choice=="Paper":
            print("You Win!!")
            count_win+=1
        elif computer_choice=="Rock" and player_choice=="Scissors":
            print("You Lose!!")
        elif computer_choice=="Paper" and player_choice=="Paper":
            print("Draw!!")
        elif computer_choice=="Paper" and player_choice=="Rock":
            print("You Lose!!")
        elif computer_choice=="Paper" and player_choice=="Scissors":
            print("You Win!!")
            count_win+=1
        elif computer_choice=="Scissors" and player_choice=="Scissors":
            print("Draw!!")
        elif computer_choice=="Scissors" and player_choice=="Paper":
            print("You Lose!!")
        elif computer_choice=="Scissors" and player_choice=="Rock":
            print("You Win!!")
            count_win+=1
    print(f"You Win {count_win} times")
    print("Thank You!!")
elif choice=="No":
    print("Thank You!!")    
else:
    raise Exception("ErrorValueInput")       