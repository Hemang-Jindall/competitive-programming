t = int(input())

for i in range(t):
    n,a,b = map(int, input().split())

    b_allowed = ((n+1)/2)
    if b < b_allowed:
        print("no")
    if a < 