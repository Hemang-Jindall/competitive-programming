# second number is n?
# 6: 3 6 4

# turns out, you have to start from the beginning, you can't just take their problem questions at face value
#descending order works totally fine

t = int(input())

for i in range(t):
    n = int(input())
    arr = list()
    while n >0:
        arr.append(n)
        n-=1

    print(*arr)