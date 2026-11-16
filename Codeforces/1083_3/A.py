# if there are 2 or more uglies, swap two random ones
# if there are 0 uglies, do nothing
# if there's 1 ugly, swap it with any (make sure it doesn't become ugly)

t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    done = False
    if n == 1:
        continue
    else:
        for j in range(n):
            if arr[j] == j +1:
                for k in range(j+1,n):
                    if arr[k] == k+1:
                        arr[j], arr[k] = arr[k], arr[j]
                        done = True
                        break
                if done == False:
                    for k in range(j+1, n):
                        if arr[k] !=k+1:
                            arr[j], arr[k] = arr[k], arr[j]
                            break

    print(*arr)
