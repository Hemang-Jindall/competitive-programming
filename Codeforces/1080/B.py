t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    for i in range(int(n/2)):
        if arr[i-1] > arr[2*i-1]:
            arr[i-1], arr[2*i-1] = arr[2*i-1], arr[i-1]
    
    if arr == sorted(arr):
        print("yes")
    else:
        print("no")