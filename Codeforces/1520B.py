t = int(input())

for _ in range(t):
    n = int(input())

    count = 0

    for digit in range(1, 10):
        num = digit

        while num <= n:
            count += 1
            num = num * 10 + digit

    print(count)