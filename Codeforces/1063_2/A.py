# 1 2 3 5 
# 3 1 2 5
# 2 1 3 5
# there must be a duplicate
# 1 2 3 3 5 6
# 3 1 3
# there must be a duplicate for every 3 elements; 4 has 2, 5 has 3 etc.
# a1​≤a2​=a3​≤a4​=a5​≤a6​=a7​≤…

# 4 2 2 1
# 1 2 2 4

t = int(input())


for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    can = True
    
    for j in range(0,n-1):
        if j % 2 != 0:
            if arr[j] == arr[j+1]:
                continue
            else:
                can = False
    if can:
        print("YES")
    else:
        print("NO")

               
