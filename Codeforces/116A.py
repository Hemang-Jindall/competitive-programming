n = int(input())
capacity = 0
max_capacity = 0

for i in range(n):
    a,b = map(int, input().split())
    capacity = b - a+capacity
    if capacity > max_capacity:
        max_capacity = capacity
print(max_capacity)

