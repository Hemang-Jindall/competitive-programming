from math import gcd

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = 2

    while True:
        ok = False

        for v in a:
            if gcd(v, x) == 1:
                ok = True
                break

        if ok:
            print(x)
            break

        x += 1