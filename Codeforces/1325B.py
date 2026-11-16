t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = len(set(a))
    
    print(s)
        