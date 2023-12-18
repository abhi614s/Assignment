'''
Write a program that accepts a string as an input from the user and calculate the
number of digits and letters. Hello123
Alph -> 5 and number -> 3
'''
str1 = input()

alph = 0
number = 0

for ch in str1:
    if ch.isalpha():
        alph += 1
    elif ch.isdigit():
        number += 1

print(f"Alph -> {alph} and number -> {number}")
