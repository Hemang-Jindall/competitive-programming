t = int(input())

for i in range(t):

    n = int(input())

    if n==2:
        print(2)
    if n==3:
        print(3)
    print(0 if n%2 == 0 else 1)