t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if n < 2 * m:
        print("NO")
        continue

    possible = True

    for i in range(m):
        if not (a[i] < b[i] < a[n - m + i]):
            possible = False
            break

    print("YES" if possible else "NO")