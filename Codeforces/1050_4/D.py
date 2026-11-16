t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))

    odds = []

    for x in d:
        if x % 2 != 0:
            odds.append(x)

    if len(odds) == 0:
        print(0)
        continue

    odds.sort()

    total = sum(d)
    remove_count = (len(odds) + 1) // 2
    removed_sum = sum(odds[:remove_count])

    print(total - removed_sum)