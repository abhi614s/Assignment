# Given an input string, write a function that returns the run length encoded string for the input string.
# Eg:
# Input: wwwwaaadebbbbbw
# Output: w4a3d1e1b5w1

def stringCompression(str1):
    count = 1 
    str2 = ""

    for i in range(len(str1)):
        if i == len(str1) - 1:
            str2 += str1[i]+str(count)
            break
        if str1[i] == str1[i+1]:
            count += 1
        else:
            str2 += str1[i]+str(count)
            count = 1
    return str2

str1 = "wwwwaaadebbbbbw"
print(stringCompression(str1))
