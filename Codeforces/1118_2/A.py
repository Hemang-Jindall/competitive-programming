# Category: Greedy
# Constraints: 1 second, 256 mb
# First instinct: Check the first and last elements using a for loop
# Other approach: Make use of libraries, euclidean algorithm
# Gotcha: 

# t = int(input())

# for _ in range(t):
#     n = int(input())

#     arr = list(map(int, input().split()))

#     def gcd(x,y):
#         if y > x:
#             drop = x
#             x = y
#             y = drop
#         for j in range(1,y+1):
#             if x % j == 0 and y % j == 0:
#                 curr = j
#         print(curr)

#     gcd(arr[0], arr[-1])
    
# big O notation: for loop (O(y+1))


t = int(input())
import math 
for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    print(math.gcd(arr[0], arr[-1]))