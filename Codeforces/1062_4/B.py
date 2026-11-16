t = int(input())

for i in range(t):
    n = int(input())
    s,t = map(str, input().split())

    sl = list(s)
    tl = list(t)
    sl.sort()
    tl.sort()

    if sl == tl:
        print("yes")
    else:
        print("no")
