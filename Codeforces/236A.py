username = str(input())

list = set(username)

count = 0

for i in list:
    count += 1


if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")