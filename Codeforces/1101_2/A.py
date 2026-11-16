# the trick is to sort the list, then choose the middle point to be the rendezvous spot, then proceed with calling everyone to meet there.
# n = number of friends
# a = friend locations

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = n

    i = 0