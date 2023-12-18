# Write a Python function that counts the number of vowels in a given string.
# Sample Input: string = "Hello, World!" Sample Output: Number of vowels: 3

str1 = "Hello Wordl!"

def vowelCount(str1):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    list1 = list(str1)

    list2 = [x for x in list1 if x in vowel]
    count = len(list2)
    
    return count


print(f"Number of vowels: {vowelCount(str1)}")
