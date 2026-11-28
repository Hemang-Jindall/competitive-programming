t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    sum = 0

    count = 0

    for i in range(n):
        while i+1 > k:
            for j in range(n):
                sum += arr[j]
            if sum % k == 0:
                count+=1

    print(count)

#time limit exceeded on test 1