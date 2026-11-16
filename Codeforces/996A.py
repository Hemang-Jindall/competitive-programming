money = int(input())
count = 0

for bill in [100,20,10,5,1]:
    count += money // bill
    money = money % bill
    
print(count)
    