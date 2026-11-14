
def solve():
    n, m, d = map(int, input().split())
    a = list(map(int, input().split()))

    # Precompute contributions of internal gaps
    g = []
    total_gap = 0

    for i in range(m - 1):
        gap = (a[i + 1] - a[i] - 1) // d
        g.append(gap)
        total_gap += gap

    best = float('inf')
    ways = 0

    # Try removing each seller
    for i in range(m):
        first = a[1] if i == 0 else a[0]
        last = a[m - 2] if i == m - 1 else a[m - 1]

        gaps = total_gap

        if i > 0:
            gaps -= g[i - 1]

        if i < m - 1:
            gaps -= g[i]

        if 0 < i < m - 1:
            gaps += (a[i + 1] - a[i - 1] - 1) // d

        prefix = (first - 1 + d - 1) // d
        suffix = (n - last) // d

        cookies = (m - 1) + prefix + suffix + gaps

        if cookies < best:
            best = cookies
            ways = 1
        elif cookies == best:
            ways += 1

    print(best, ways)


t = int(input())

for _ in range(t):
    solve()
