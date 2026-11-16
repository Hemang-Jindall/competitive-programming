t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    is_there = False
    found = -1

    for j in range(n):
        if a.count(a[j]) >= 3:
            is_there = True
            found = a[j]
            break

    if is_there:
        print(found)
    else:
        print(-1)