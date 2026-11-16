t = int(input())

for i in range(t):
    n = int(input())
    integers_array = list(map(int, input().split()))

    if len(set(integers_array)) == len(integers_array):
        print("YES")
    else:
        print("NO")