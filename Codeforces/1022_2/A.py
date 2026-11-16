# Problem: A. In the Dream
# One sentence: Check if goals in each half could happen without 3-in-a-row for either team.
# Category: Math/constructive.
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Find max allowed ratio between two teams' goals in a half.
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).

t = int(input())

for _ in range(t):
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(i + 1)

    arr_r = arr[::-1]

    max_f = 0
    for i in range(n):
        max_f += abs(arr_r[i] - arr[i])

    possible_values = (max_f // 2) + 1

    print(possible_values)