t = int(input())

for i in range(t):
    n = int(input())

    counts = {}

    for j in range(n):
        row = list(map(int, input().split()))

        for c in row:
            counts[c] = counts.get(c,0) + 1

    max_count = max(counts.values())

    if max_count <= n*n-n:
        print("YES")
    else:
        print("NO")

    
