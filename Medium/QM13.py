# Write a Python program to find if a given string starts with a given character using Lambda.
# Sample input: input_string = "Hello, World!", given_char = "H" 
# Sample Output: True

str1 = input('Enter string: ')
char1 = input('Enter the char: ')[0]

start = lambda string, char : string.startswith(char)

print(start(str1, char1))

# resolved
