# Category: Greedy
# Constraints: t large, values big -> need O(n) per test case.
# First instinct: Sort the array and compare the two middle elements.
# Other approach: Separate elements by parity of their positions and compare the ranges.
# Gotcha: Sorting destroys positional information. The condition depends on which elements are at odd/even positions, not just on their values.


t = int(input())

for i in range(t):

    n, m = map(int, input().split())
    possible_words = list()
    possible = True
    for k in range(n):
        new_string = input()
        possible_words.append(new_string[0].upper())

    for j in range(m):
        ab_string = input()
        for h in range(len(ab_string)):
            if ab_string[h] not in possible_words:
                possible = False

    if possible:
        print("YES")
    else:
        print("NO")