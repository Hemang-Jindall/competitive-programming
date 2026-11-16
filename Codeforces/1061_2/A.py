# first thought, the strategy is to have the last partition always be 3 (if possible)

t = int(input())

for i in range(t):
    n = int(input())

    print((n - 1) // 2)