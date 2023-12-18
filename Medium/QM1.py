# Write a Python program to find the common elements between two lists.
# Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8] 
# Sample output: [4, 5]

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8,9]

common_list = [element for element in list1 if element in list2]
print(common_list)
