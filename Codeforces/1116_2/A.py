t = int(input())

for i in range(t):
    smallest, middle, largest = sorted(map(int, input().split()))
    if (smallest + middle) < largest:
        print((smallest + middle) - smallest)
    else:
        print(largest - smallest)