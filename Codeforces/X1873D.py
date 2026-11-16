t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    i = 0
    ans = 0

    while i < n:
        if s[i] == 'B':
            ans += 1
            i += k
        else:
            i += 1

    print(ans)