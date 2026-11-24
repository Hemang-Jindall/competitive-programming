def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    m = n - k + 1

    pref = [0] * n

    for i in range(1, n):
        pref[i] = pref[i - 1] + (a[i] != a[i - 1])

    ans = 0

    for l in range(k):
        r = l + m - 1

        if pref[r] - pref[l] == 0:
            ans += 1

    print(ans)


t = int(input())

for _ in range(t):
    solve()