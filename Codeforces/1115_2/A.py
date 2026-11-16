t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    prev = None
    damage = 0

    while arr:
        curr = None
        curr_index = -1

        for j in range(len(arr)):
            if arr[j] != prev:
                if curr is None or arr[j] > curr:
                    curr = arr[j]
                    curr_index = j

        if curr is None:
            damage += arr[0]
            break

        damage += curr
        prev = curr
        arr.pop(curr_index)

    print(damage)