t = int(input())

for _ in range(t):
    input()  # read n and ignore it
    arr = list(map(int, input().split()))
    print("YES" if 67 in arr else "NO")