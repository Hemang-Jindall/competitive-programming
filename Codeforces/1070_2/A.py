# Problem: A. Operations with Inversions
# One sentence: Find out the max no. of operations possible
# Category: Math/constructive.
# Constraints: 1 second time limit; 256 mb memory limit
# First instinct: loop through the array, count how many smaller numbers occur before larger ones.
# Other approach: First approach worked out.
# Gotcha: None.

t = int(input())

for l in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    indexes_seen = list()
    
    # i is the first index and larger and stays

    for i in range(n):
        for j in range(i,n):
            if arr[i] > arr[j] and j not in indexes_seen:
                count+=1
                indexes_seen.append(j)
    print(count)