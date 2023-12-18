# Write a Python program to reverse a number using a while loop.
# Sample Input: num = 12345 Sample Output: revnum = 54321

num = 123
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem 
    num //= 10

print(rev)
