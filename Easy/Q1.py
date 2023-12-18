'''
Write a program in Python to perform the following operation:
● If a number is divisible by 3 it should print “Brudite” as a string
● If a number is divisible by 5 it should print “Python Training” as a string 
● If a number is divisible by both 3 and 5 it should print “Brudite - Python Training” as a string.
'''

response = int(input())

if response % 3 == 0:
    print("Brudite")
    
if response % 5 == 0:
    print("Python Training")

if (response % 3 == 0) and (response % 5 == 0):
    print("Brudite - Python Training")
