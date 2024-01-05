'''
Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:

Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.

'''

def read_even_length_strings(filename):

    with open(filename, 'r') as file:
        even_strings = []
        
        for line in file:
            words = line.split()
            even_words = [word for word in words if len(word) % 2 == 0]
            even_strings.extend(even_words)
    
    return even_strings

even_strings = read_even_length_strings('Advance/doc.txt')
print(even_strings)
