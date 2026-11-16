# Problem: A. You Delete, I Delete
# Category: Greedy
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Loop through twice
# Other approach:
# Gotcha: 

#alice deletes leftmost 0s
#bob deletes the leftmost 1s

t = int(input())

for _ in range(t):
    arr = list(input())

    #alice
    for i in range(len(arr)):
        if arr[i] == "0":
            arr.pop(i)
            break

    #bob
    for j in range(len(arr)):
        if arr[j] == "1":
            arr.pop(j)
            break

    print("".join(arr))