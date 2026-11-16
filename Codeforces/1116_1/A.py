# Problem: A. You Delete, I Delete
# Category: Greedy
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Loop through twice
# Other approach:
# Gotcha: 

# odd leps are red, even leps are blue
# k rounds
# 2n leps
# the lep can pass the potato clockwise
# 

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = input()
    
