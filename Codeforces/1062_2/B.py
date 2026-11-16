
t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    s = input()

    a = s.count('4')
    b = s.count('8')

    if abs(x) + abs(y) <= a + 2 * b and max(abs(x), abs(y)) <= a + b:
        print("YES")
    else:
        print("NO")
