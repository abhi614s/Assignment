'''
Write a Python program to check if a string is an anagram of another string.
string1 = "listen", string2 = "silent"
Output: True
'''

def checkAnagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    anagram = True
    if len(str1) != len(str2):
        anagram = False
        return anagram 
    
    char_count = {}
    
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            anagram = False
            return anagram 
        else:
            char_count[char] -= 1

    return anagram

response = checkAnagram("listen","silent")
print(response)
