t = int(input())

for _ in range(t):
    n = int(input())
    k = n // 2

    if k % 2 == 1:
        print("NO")
        continue

    even = [2 * i for i in range(1, k + 1)]
    odd = [2 * i - 1 for i in range(1, k)]

    odd.append(sum(even) - sum(odd))

    print("YES")
    print(*even, *odd)