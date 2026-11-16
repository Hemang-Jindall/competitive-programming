t = int(input())

for i in range(t):

    x,y = map(int, input().split())

    x_in, y_in = 0,0

    x_allowed = ["2", "3", "4"]
    y_allowed = ["1", "0", "-1"]

    possible = True

    while x_in != x:
        if x-x_in == 1:
            possible = False
        if x==x_in and y_in != y:
            possible = False
            