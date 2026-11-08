

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    c  = arr.count(arr[0])
    if k < c:
        print("NO")
    else:
        print("YES")
        print(*arr[:k][::-1] + arr[k:])
        
