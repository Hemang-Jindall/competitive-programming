t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    s = sum(arr)

    if s % 2 == 0 and s // 2 in arr:
        print(-1)
    else:
        arr.sort(reverse=True)
        print(*arr)