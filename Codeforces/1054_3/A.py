# -1, 0 or 1
# if you see 0, increase operation count by 1, if there's an odd number of -1s, increase operation count by 2


t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    neg_count = 0
    for i in range(n):
        if arr[i] == 0:
            count+= 1
        elif arr[i] == -1:
            neg_count +=1
    if neg_count % 2 != 0:
        count+= 2

    print(count)