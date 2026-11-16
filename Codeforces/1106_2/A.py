# Problem: A. Another Puzzle from Papyrus

# What is this asking me to do in one sentence?
# Convert a to b in the smallest amount of time possible.

# What category does this feel like?
# This is a greedy/exchange-argument problem

# What are the constraints telling me?
# Time limit is 1 second per test, don't know what that tells me yet.
# Memory limit is 256 mb, don't know what that insinuates either.

# What's my first instinct?
# If elements are same in both, just reorder; if a is less than b in total sum, print -1; if a is more than b, calculate the difference in total sum and see if its more than reordering it

# Is there another approach?
# Can't think of one.


t = int(input())

for i in range(t):

    n,c = map(int, input().split())

    a = list(map(int, input().split()))

    b = list(map(int, input().split()))
    feasible = True
    impossible = False
    cost = 0

    for j in range(n):
        if a[j] >= b[j]:
            continue
        else:
            feasible = False

    aSorted = sorted(a)
    bSorted = sorted(b)

    if feasible == False:
        for w in range(n):
            if aSorted[w] >= bSorted[w]:
                continue
            else:
                impossible = True
                break
        cost += c

    cost += sum(a) - sum(b)
    if impossible:
        print(-1)
    else:
        print(cost)


