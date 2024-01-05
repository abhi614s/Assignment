'''
Write a Python program to check if a given number is a perfect number.
'''

num = int(input("Enter a number: "))
sum = 0

for i in range(1,(num//2)+1):
    if num % i == 0 and i != num:
        sum += i

if num == sum:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
