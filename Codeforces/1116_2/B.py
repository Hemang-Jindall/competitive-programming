t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0

    for common in range(1, m + 1):
        curr = 0

        for j in range(n):
            if arr[j] == common:
                curr += 1
            elif arr[j] > common:
                curr += 1

                if arr[j] == 2 * common:
                    curr += 1

        ans = max(ans, curr)

    print(ans)