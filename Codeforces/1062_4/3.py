l = int(input())

for i in range(l):
    n = int(input())
    even_sum = 0
    odd_sum = 0
    t = list(map(int, input().split()))

    def odd(x):
        if x % 2 != 0:
            return True
    def even(x):
        if x % 2== 0:
            return True
    
    for i in range(n):
        if even(t[i]):
            even_sum +=1
        elif odd(t[i]):
            odd_sum +=1 
    
    if even_sum == n or odd_sum== n or even_sum == 0 or odd_sum == 0:
        print(t)
    else:
        t.sort()
        print(*t)