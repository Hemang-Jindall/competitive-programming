number_of_drinks = int(input())
volume_fraction = list(map(int, input().split()))
result = sum(volume_fraction)/ (number_of_drinks)
print(result)
