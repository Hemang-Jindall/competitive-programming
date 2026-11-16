t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    s = sum(arr)

    max = max(arr)

    if s < 0:
        max += -s
    else:
        max += s
    print(max)