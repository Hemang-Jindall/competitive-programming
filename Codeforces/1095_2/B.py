# from functools import reduce
# from math import gcd

# t = int(input())

# for _ in range(t):

#     n = int(input())
#     arr = list(map(int, input().split()))

#     ans = 0

#     for i in range(n):
#         for j in range(i,n):
#             subarray = arr[i:j+1]
#             if max(subarray)- min(subarray) == reduce(gcd, subarray):
#                 ans +=1
#     print(ans)

