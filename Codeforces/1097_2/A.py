# to optimize, start from the last digit backwards. 
# 1 2 3
# 1 2 3
# 1 3 3
# 1 3 6

# 3 2 1
# 3 3 1
# 6 3 1

# 100 -100
# -100 100
# -100 0
# 100 -100
# 100 -100
# 0 -100

# t = int(input())

# for i in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     arr.reverse()

#     for j in range(1,n):
#         arr[j] = arr[j] + arr[j-1]

#     positive = 0
#     for i in arr:
#         if i > 0:
#             positive +=1 

#     print(positive)


# sub optimal, we have to take into account negative numbers


t = int(input())

for i in range(t):
    