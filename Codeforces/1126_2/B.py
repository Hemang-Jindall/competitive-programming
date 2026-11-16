t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    arr = list(map(int, input().split()))

    set_arr = set(arr)

    freq = [0] * (n+1)

    for x in arr:
        freq[x] += 1

    mex = 0

    while freq[max] >=k:
        print("YES")
    else:
        print("NO")
