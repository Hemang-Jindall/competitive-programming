number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    a,b,c = map(int, input().split())
    if a+b == c or a+c == b or b+c == a:
        print("YES")
    else:
        print("NO")