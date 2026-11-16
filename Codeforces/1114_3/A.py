t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())

    if a == b or b== c or c == a:
        print(0)
    else:
        print(min(abs(a-b), abs(b-c), abs(c-a)))