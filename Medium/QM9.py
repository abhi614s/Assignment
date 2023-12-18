# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

list1 = [1,2,3,4,5]

for i in range(0,len(list1)):
        try:
            temp = list1[i] 
            list1[i] = list1[i+1]
            list1[i+1] = temp
        except IndexError:
            print("Array Index is exceeding it's maximum value")
