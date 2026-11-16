t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    i_count = arr.count(1)
    j_count = arr.count(0)

    if i_count > j_count:
        print("YES")
    else:
        print("NO")