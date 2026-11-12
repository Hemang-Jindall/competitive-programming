t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * (n + 1)

    for x in a:
        freq[x] += 1

    best_l = -1
    best_r = -1
    best_len = 0

    i = 0

    while i < n:
        if freq[a[i]] != 1:
            i += 1
            continue

        j = i

        while j < n and freq[a[j]] == 1:
            j += 1

        length = j - i

        if length > best_len:
            best_len = length
            best_l = i + 1
            best_r = j

        i = j

    if best_len == 0:
        print(0)
    else:
        print(best_l, best_r)