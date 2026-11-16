n = int(input())

for i in range(n):
    t = input()

    t_list = list(t)

    if int(t_list[0]) + int(t_list[1]) + int(t_list[2]) == int(t_list[3]) + int(t_list[4]) + int(t_list[5]):
        print("YES")
    else:
        print("NO")