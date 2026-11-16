t = int(input())

for _ in range(t):

    n = int(input())

    weights = list(map(int, input().split()))

    ones = weights.count(1)
    twos = weights.count(2)

    total = ones + 2 * twos

    if total % 2 != 0:
        print("NO")

    elif ones == 0 and twos % 2 != 0:
        print("NO")

    else:
        print("YES")