t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    total = 0
    if n == k:
        print(2*n)
    else:
        remaining = n-k + 1
        total += (k-1)*2
        total += 2 **remaining
        print(total)
        
    
