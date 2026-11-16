t = int(input())

for i in range(t):
    a = list(map(int, input().split()))

    a.sort()
    
    for i in range(len(a)-1):
        a[i] *=-1

    print(sum(a))