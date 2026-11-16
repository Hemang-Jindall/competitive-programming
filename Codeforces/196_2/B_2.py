t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    best = 0

    for x in set(s):
        total = sum(1 for y in s if y % x == 0)
        best = max(best, total)

    print(n-best)