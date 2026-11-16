t = int(input())

for i in range(t):
    x,y = map(int, input().split())

    def even(num):
        if num % 2 == 0:
            return True
        
    if even(x) and even(y):
        print("YES")
    elif even(x) and not even(y):
        print("YES")
    elif not even(x) and even(y):
        print("YES")
    else:
        print("NO")