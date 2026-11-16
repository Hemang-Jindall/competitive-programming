t = int(input())

for _ in range(t):

    s = input()

    n = len(s)
    m = n // 2

    if n % 2 != 0:
        print("NO")
        continue

    good = True

    for i in range(m):

        if s[i] != s[m + i]:
            good = False
            break

    if good:
        print("YES")
    else:
        print("NO")