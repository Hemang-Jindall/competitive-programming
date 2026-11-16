# Problem: A. Sleeping Through Classes
# What is this asking me to do in one sentence?: Find the maximum amount of classes you can sleep through.
# What category does this feel like? Feels like an array problem.
# What are the constraints telling me? 
# What's my first instinct? Go through array one by one
# Is there another approach?
# What's the gotcha / edge case? 

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    sleep = 0
    awake = 0

    for c in s:
        if c == '1':
            awake = k
        elif awake > 0:
            awake -= 1
        else:
            sleep += 1

    print(sleep)