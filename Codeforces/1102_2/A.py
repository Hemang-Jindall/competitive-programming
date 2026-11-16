t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort(reverse=True)

    good = True

    for i in range(n - 2):
        if b[i] % b[i + 1] != b[i + 2]:
            good = False
            break

    if good:
        print(b[0], b[1])
    else:
        print(-1)