# Write a program to count the the lines in a file “demo.txt”

def count_lines(filename):
    
    with open(filename, 'r') as file:
        return len(file.readlines())

line_count = count_lines('Advance/demo.txt')
print(f"The file '{'Advance/demo.txt'}' has {line_count} lines.")
