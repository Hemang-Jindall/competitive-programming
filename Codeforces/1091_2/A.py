t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    s = sum(arr)

    if (n * k) % 2 == 0 or s % 2 == 1:
        print("YES")
    else:
        print("NO")