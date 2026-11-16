# Category: Greedy
# Constraints: t large, values big -> need O(n) per test case.
# First instinct: Sort the array and compare the two middle elements.
# Other approach: Separate elements by parity of their positions and compare the ranges.
# Gotcha: Sorting destroys positional information. The condition depends on which elements are at odd/even positions, not just on their values.


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    
    for i in range(n):
        if a[i] == "1":
            if i != 0 and b[i-1] == "0":
                a[i] = "0"
                b[i-1] = "1"
            elif i != n-1 and b[i+1] == "0":
                a[i] = "0"
                b[i+1] = "1"

    if a.count("1") == 0:
        print("yes")
    else:
        print("no")