#total number of crossings is the sum of vertical and horizontal lasers

t = int(input())

for i in range(t):
    n,m,x,y = map(int, input().split())
    y_cords= list(map(int, input().split()))
    x_cords = list(map(int, input().split()))

    print(n+m)
