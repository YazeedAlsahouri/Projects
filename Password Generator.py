import random
print("This Project will generate a password!!")
count_passwords=int(input("Enter how many passwords do you want to generate: "))
char_in_password="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890_*/"
for i in range(count_passwords):
    password_length=int(input("Enter the length of your password: "))
    password=""
    for j in range(password_length):
        random_char=random.choice(char_in_password)
        password+=random_char
    print(f"Your password is ({password})")
