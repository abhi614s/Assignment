# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

# Sample Input: n = 7
# Sample Output: Stones in a single pile = [7, 9, 11, 13, 15, 17, 19]

n = 7

def stonePiles(n):
    list1 = []
    i = 1
    j = 0

    while i <= n:
        list1.append(n+j)
        i += 1
        j += 2
        
    return list1

print(stonePiles(n))
