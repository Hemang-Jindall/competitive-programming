t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    possible = True

    for start in range(k):
        ones = 0
        i = start

        while i < n:
            if s[i] == '1':
                ones += 1
            i += k

        if ones % 2 == 1:
            possible = False
            break

    print("YES" if possible else "NO")