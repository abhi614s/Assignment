'''
Write a Python program to reverse the order of words in a given sentence.
input_sentence = “Hello, World! Welcome to Python programming.” 
Output after reverse = “programming. Python to Welcome World! Hello,”
'''

str1 = input()

list1 = str1.split()
rev_str = str(list1[::-1])

print(rev_str)
