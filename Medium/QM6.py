# Write a Python program to check if a number is a power of two using recursion.

num = int(input())

def powOfTwo(num):
    while num > 1:
        if num % 2 != 0:
            return False
            break

        num /= 2
    return True

print(powOfTwo(num))
