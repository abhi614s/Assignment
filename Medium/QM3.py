# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
# SampleInput:arr=[1,2,3,4,5], k=6
# Sample Output: Pair count: 2

def pairCount(list1, k):
    count = 0
    for i in range(0, len(list1) - 1):
        for j in range(0, len(list1) - 1):
            if i == j:
                continue
            else:
                if(list1[i] + list1[j]) == k:
                    count += 1
    return count

list1 = [1,2,3,4,5]
k = 6

print(f"Pair count: {pairCount(list1,k)}")
