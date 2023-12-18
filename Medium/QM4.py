# Given an array of size N The task is to rotate array by D elements towards right
# Sample Input: arr = [1, 2, 3, 4, 5], D = 2
# Sample Output: arr after rotation = [4, 5, 1, 2, 3]

list1 = [1, 2, 3, 4, 5]
d = 2

def rotateArray(list1, d):
    list1 = list1[-d:] + list1[:-d]
    return list1

# Print the rotated array
print(rotateArray(list1,d))
