t = int(input())

for _ in range(t):

    n = int(input())

    integer_list = list(map(int, input().split()))

    smallest = 0

    for i in range(n):

        if integer_list[i] < integer_list[smallest]:
            smallest = i

    integer_list[smallest] += 1

    product = 1

    for i in range(n):
        product *= integer_list[i]

    print(product)