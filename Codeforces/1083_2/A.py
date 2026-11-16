t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ugly = []
    mx = 0

    for i in range(n):
        mx = max(mx, arr[i])
        if mx == i + 1:
            ugly.append(i)

    if len(ugly) >= 2:
        arr[ugly[0]], arr[ugly[-1]] = arr[ugly[-1]], arr[ugly[0]]

    print(*arr)