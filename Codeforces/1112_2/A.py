# Problem: A. Threshold Movement
# Category: Greedy
# Constraints: t large, values big -> need O(n) per test case.
# First instinct: Sort the array and compare the two middle elements.
# Other approach: Separate elements by parity of their positions and compare the ranges.
# Gotcha: Sorting destroys positional information. The condition depends on which elements are at odd/even positions, not just on their values.

t = int(input())
for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    sorted_arr = sorted(arr)

    if n % 2 == 0:
        if sorted_arr[n//2] - sorted_arr[n//2 -1] <= 1:
            print("no")
        else:
            print("yes")
    else:
        print('no')

