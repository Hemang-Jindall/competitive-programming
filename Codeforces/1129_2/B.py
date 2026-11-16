t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if min(a) < n:
        print(n)
    else:
        print(0)