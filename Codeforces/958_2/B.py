# Category: greedy, implementation, *900
# Constraints: 1.5 seconds, 512 mb
# First instinct: compare the count of groups of 0s and count of 1s
# Improvemnet: Coudln't figure out the actual code for a change

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    ones = 0
    zero_groups = 0
    prev = '1'

    for x in a:
        if x == '1':
            ones += 1
        if x == '0' and prev == '1':
            zero_groups += 1
        prev = x

    if (ones > zero_groups):
        print("YES")
    else:
        print("NO")
        