
t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 0:
        print(-1)
    else:
        p = list(range(1, n + 1))

        for i in range(1, n - 1, 2):
            p[i], p[i + 1] = p[i + 1], p[i]

        print(*p)


#identified the pattern pretty quickly
#note to self: don't fucking give up