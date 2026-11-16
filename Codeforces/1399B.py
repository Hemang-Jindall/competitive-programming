t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minA = min(a)
    minB = min(b)

    ans = 0

    for i in range(n):
        ans += max(a[i] - minA, b[i] - minB)

    print(ans)