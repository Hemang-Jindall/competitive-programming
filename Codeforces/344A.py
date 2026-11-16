number_of_magnets = int(input())
count = 1
previous = input()
for i in range(number_of_magnets - 1):
    current = input()
    if current != previous:
        count += 1
    previous = current
print(count)