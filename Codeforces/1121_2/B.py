# Categories: Greedy, Data Structures
# Constraints: O(n log n), O(n)
# First instinct: Choose the lowest elements besides the last one
# Gotcha: Sorting destroys positional information. The condition depends on which elements are at odd/even positions, not just on their values.

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    for i in range(n):
        