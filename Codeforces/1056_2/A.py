# 2: 1 + 1 
# 3: 1+1 + 1 + 1
# 4: 1+1+1 + 1 + 1
# 5: 1+1+1+1 + 1 + 1 + 1
# 6: 1+1+1+1+1 + 1 + 1 + 1
# 7: 1+1+1+1+1+1 + 1 + 1 + 1 + 1
# 8: 1+1+1+1+1+1+1 + 4
# 9: 8 + 5
# 10: 9 + 5
# the winner's is just one lower than the total, and the losers is half if even, half + 1 if odd except for a few lower ones


t = int(input())

for _ in range(t):
    n = int(input())
    print(2 * n - 2)
