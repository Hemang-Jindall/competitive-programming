t = int(input())

for _ in range(t):
    n = int(input())
    arr = input()

    curr_biggest = 0
    biggest = 0

    for i in range(n):
        if arr[i] == "#":
            curr_biggest += 1

            if curr_biggest > biggest:
                biggest = curr_biggest
        else:
            curr_biggest = 0

    print((biggest + 1) // 2)