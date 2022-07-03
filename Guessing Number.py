import random
choose=input("Do you want to play Guessing number game?(Yes/No): ")
if choose=="Yes" or choose=="yes":
    random_number=random.randint(0,101)
    guess_number=int(input("Enter your guess: "))
    counter=1
    while guess_number!=random_number:
        if guess_number>random_number:
            print("Your guess is high")
        elif guess_number<random_number:
            print("Your guess is low")
        guess_number=int(input("Try again: "))
        counter+=1
    print(f"Congratulation you guessed the number after {counter} times!!!")
    print("Thank You!!")
elif choose=="No" or choose=="no":
    print("Thank You!!")
else:
    raise Exception("ValueInputError")
