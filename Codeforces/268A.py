n = int(input())
b_list = list()
a_list = list()
count = 0
for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

for i in a_list:
    for j in b_list:
        if i == j:
            count += 1
print(count)