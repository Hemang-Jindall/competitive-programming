# Problem:
# Rating:
# Topic:

# My approach:
# Why it worked / failed:

# Key insight:

# Mistake:

# Complexity:

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    new_arr = sorted(arr, reverse = True)
    j = 0
    ans_arr = list()

    for i in range(len(n)):
        if new_arr[i] not in ans_arr:
            ans_arr[j] = new_arr[i]
            j+=1
            new_arr.pop(i)

    