# we try to keep duplicate elements, we try to keep elements that are multiples of other elements, we try to keep smaller elements
# ill check for the smallest element, see how many multiples it has, and subtract that number from the total number of elements

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))

#     s.sort()
#     total = 0
#     max_count = 0
#     best_element = None

#     for i in range(n):
#         total = 0
#         for j in range(n):
#             if s[j] % s[i] == 0:
#                 total +=1
#         if total >= max_count:
#             max_count = total
#             best_element = s[i]

#     print(n - max_count)

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    best = 0

    for x in set(s):
        total = sum(1 for y in s if y % x == 0)
        best = max(best, total)

    print(n - best)

# Improvements:

# sort mistake
# I don't excatly still get line 35 of the code