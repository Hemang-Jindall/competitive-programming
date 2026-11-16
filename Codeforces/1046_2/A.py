# Problem: A. In the Dream
# One sentence: Check if goals in each half could happen without 3-in-a-row for either team.
# Category: Math/constructive.
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Find max allowed ratio between two teams' goals in a half.
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).


t = int(input())

for i in range(t):
    a,b,c,d = map(int, input().split())
    fucked = False
    if a >=b:
        if a -b >3:
            fucked = True
    if b>=a:
        if b-a >3:
            fucked = True
    
    if c >=d:
        if c -d >3:
            fucked = True
    if d>=c:
        if d-c >3:
            fucked = True

    if fucked:
        print('no')
    else:
        print("yes")
    
        