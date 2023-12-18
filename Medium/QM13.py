# Write a Python program to find if a given string starts with a given character using Lambda.
# Sample input: input_string = "Hello, World!", given_char = "H" 
# Sample Output: True

str1 = input('Enter string: ')
char1 = input('Enter the char: ')[0]

def checkStart(str1, char1):
    if str1[0] == char1:
        return True
    else:
        return False

print(checkStart(str1, char1))
