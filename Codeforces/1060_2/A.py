t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    arr = list(map(int, input().strip()))

    ans = 0
    fine = False
    num = 0

    for j in range(n):
        if j == 0:
            if arr[j] == 1:
                fine = True
                ans += 1
                num = 0

        if j > 0 and arr[j] == 1 and fine == False:
            ans += 1
            fine = True
            num = 0

        elif arr[j] == 1 and fine == True:
            num = 0

        if fine:
            num += 1
            if num >= k:
                fine = False

    print(ans)