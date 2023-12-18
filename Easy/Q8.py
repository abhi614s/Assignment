'''
Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
'''
import math 

def findLcm(num1, num2):
    gcd = math.gcd(num1,num2)
    return (num1*num2)//gcd

print(findLcm(14,32))
