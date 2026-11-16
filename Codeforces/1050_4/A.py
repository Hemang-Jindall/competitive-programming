# if it's even, it'll be 0, if it' odd, it's be x


t = int(input())

for i in range(t):
    x, n = map(int, input().split())

    if n % 2 == 0:
        print(0)
    else:
        print(x)