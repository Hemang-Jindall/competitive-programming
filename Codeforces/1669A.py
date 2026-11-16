n = int(input())

for i in range(n):
    r = int(input())

    if r <= 1399:
        print("Division 4")

    elif 1400 <= r <= 1599:
        print("Division 3")

    elif 1600 <= r <= 1899:
        print("Division 2")

    else:
        print("Division 1")