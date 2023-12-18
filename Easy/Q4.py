'''
Write a Python program to find the sum of all odd numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
'''

print("Enter start and end")
start, end = map(int, input().split())

sum = 0

for num in range(start, end+1):
    if num % 2 != 0:
        sum += num

print(f"sum of all odd numbers between {start} and {end} = {sum}")
