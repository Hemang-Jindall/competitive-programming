t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    largest = max(a, b, c)
    smallest = min(a, b, c)

    middle = a + b + c - largest - smallest

    print(middle)