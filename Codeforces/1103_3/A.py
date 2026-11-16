t = int(input())

for i in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    h.sort()

    k = (h[-1]+1)-h[0]
    print(k)