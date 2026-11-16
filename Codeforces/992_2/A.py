# Problem: A. Game of Division
# One sentence: Make the first player win by finding an index i where |a_i - a_j"| / k != whole number
# Category: Math/constructive.
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Loop through it
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    found = False

    for j in range(n):
        works = True

        for i in range(n):
            if i != j:
                if abs(arr[j] - arr[i]) % k == 0:
                    works = False
                    break

        if works:
            ans = j
            found = True
            break

    if found:
        print("YES")
        print(ans + 1)
    else:
        print("NO")