t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    mn = float('inf')
    ans = 0

    for x in arr:
        mn = min(mn, x)
        ans += mn

    print(ans)


#https://chatgpt.com/c/6a34d2cb-fccc-83e8-b76d-fe81824276e6