# Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
# Sample Input: num = 9876
# Sample Output: Sum_of_digits = 3

num = 9876

def singleDigitSum(num):
    while num >= 10:
        digit_sum = 0

        while num > 0:
            digit_sum += num % 10
            num //= 10
        
        num = digit_sum
    return num

print(singleDigitSum(num))
