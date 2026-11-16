t = int(input())

for _ in range(t):

    n,m = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    possible_1 = 0
    possible_2 = 0

    for i in range(0,n-1):
        possible_1 += arr_1[i] - arr_1[i+1] + 1
    for j in range(0,m-1):
        possible_2 += arr_2[j] - arr_2[j+1] + 1

    possible_1 += arr_1[-1]
    possible_2 += arr_2[-1]
    if possible_1 > possible_2 or possible_1 == possible_2:
        print(1)
    else:
        print(2)