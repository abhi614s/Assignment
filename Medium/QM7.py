# Write a Python function that finds the median of a list of numbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3] Sample Output: Median: 4.5


list1 = [7, 2, 5, 1, 9, 3]
sorted_list = [1, 2, 3, 5, 7, 9]

def findMedian(list1):
    mid = int(len(list1)/2)
    
    if len(list1) % 2 == 0:
        return (list1[mid-1] + list1[mid])/2
    else:    
        return list1[mid]

print(findMedian(list1))
