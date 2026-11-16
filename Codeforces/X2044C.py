t = int(input())
for i in range(t):
    m,a,b,c = map(int, input().split())

    row_1 = m
    row_2 = m

    count = 0

    while row_1 >0 and a > 0:
        row_1 -= 1
        a -= 1
        count+=1

    while row_2 >0 and b > 0:
        row_2 -= 1
        b -= 1
        count+=1
    
    while row_1 > 0 and c > 0:
        row_1 -=1
        c -=1
        count+=1

    while row_2 > 0 and c > 0:
        row_2 -=1
        c -=1
        count+=1    

    print(count)




t = int(input())

for _ in range(t):
    m, a, b, c = map(int, input().split())

    count = min(a, m) + min(b, m)

    remaining = (m - min(a, m)) + (m - min(b, m))

    count += min(c, remaining)

    print(count)