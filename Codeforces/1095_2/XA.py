# optimize cost
# maintain non-decreasing condition

# 2 5 6 3 6

# 2 * 5 * 6, 3 * 6 = 78
# 2 * 5, 6, 3 *6 = 40
# 2, 5, 6, 3, 6 = 22

#basically, you never multiply except with 1s


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = sum(x for x in a if x > 1)

    if a[-1] == 1:
        ans += 1

    print(ans % 676767677)

# reversing the array, FUCK