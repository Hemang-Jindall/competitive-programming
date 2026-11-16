t = int(input())

for i in range(t):
    n =int(input())
    s = list(map(int, input().split()))
    max_s = max(s)

    temp = s.copy() 
    temp.remove(max_s)

    second_max = max(temp)

    max_s = max(s)
    new_s = list()
    for i in range(n):
            if s[i] == max_s:
                 new_s.append(s[i] - second_max)
            else:
                new_s.append(s[i] - max_s)

    print(*new_s)