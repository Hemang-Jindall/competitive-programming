t = int(input())

for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    minimum = 1000
    for j in range(n):
        for k in range(n):
            if s[j] - s[k] < minimum and s[j] - s[k] >= 0 and j !=k:
                minimum = s[j] - s[k]
    print(minimum)

