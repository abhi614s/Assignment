'''
Write a Python program to count the frequency of each element in a list.
input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
'''

def freqCounter(list1):
    count = {}
    for num in list1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count
