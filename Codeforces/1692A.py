n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())

    ahead = 0

    if b > a:
        ahead += 1

    if c > a:
        ahead += 1

    if d > a:
        ahead += 1

    print(ahead)