# Create a function that takes a list and returns a new list with unique elements of the first list.
# Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5] Sample Output: list2 = [1, 2, 3, 4, 5]

def uniqueElement(list1):
    set1 = set(list1)
    list2 = list(set1)
    return list2

list1 = [1,1,1,2,3,3,3,4,5,5,5,5]
list2 = uniqueElement(list1)
print(list2)
