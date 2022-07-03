# -*- coding: utf-8 -*-
"""
This Code Will generate a password
"""
import random
number_of_passwords=int(input("Enter gow many passwords you want: "))
for i in range(number_of_passwords):
    password=""
    char="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM.*_1234567890"
    length_password=int(input(f"Enter the length of password number {i+1}: "))
    for j in range(length_password):
        random_char=random.choice(char)
        password+=random_char
    print(f"You Password is ({password})")