r, b = map(int, input().split())

count = 0

while r > 0 and b > 0:
    count += 1
    r -= 1
    b -= 1

same = max(r, b) // 2

print(count, same)