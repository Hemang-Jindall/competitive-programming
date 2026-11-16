# Problem: A. Game of Division
# One sentence: Make the first player win by finding an index i where |a_i - a_j"| / k != whole number
# Category: Math/constructive.
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Loop through it
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    distinct = len(set(arr))

    while distinct not in arr:
        arr.append(distinct)
        distinct +=1

    print(distinct)

