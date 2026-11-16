t = int(input())

for i in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    a = sorted(set(a))

    best = 1 
    curr =1

    for i in range(1, len(a)):
        if a[i] == a[i-1] + 1:
            curr +=1
        else:
            best = max(curr, best)
            curr = 1
    best = max(curr, best)
    print(best)