# Problem: A. Little Fairy's Painting
# Category: Greedy
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Loop through twice
# Other approach:
# Gotcha: 

#alice deletes leftmost 0s
#bob deletes the leftmost 1s

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    distinct = len(set(arr))

    while distinct not in arr:
        arr.append(distinct)
        distinct +=1
    print(distinct)