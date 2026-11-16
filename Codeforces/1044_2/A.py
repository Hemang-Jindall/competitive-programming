# Problem: A. Redstone?
# One sentence: Find out if the rightmost gear can rotate at 1 rev/sec.
# Category: 
# Constraints: 
# First instinct: 
# Other approach: 
# Gotcha: 







t = int(input())

for i in range(t):
    n = int(input()) #number of gears
    arr = list(map(int, input().split())) #teeth of each gear

    if len(set(arr)) == len(arr):
        print('no')
    else:
        print("yes")
