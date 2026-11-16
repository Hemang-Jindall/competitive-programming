k,n,w = map(int, input().split())

#k = cost of first banana
#n = dollars he has
#w = bananas he wants to buy

cost = 0
borrow = 0

for i in range(w):
    cost += k*(i+1)

if cost > n:
    borrow = cost - n

print(borrow)