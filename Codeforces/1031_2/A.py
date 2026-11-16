# Problem: A. Shashliks
# What is this asking me to do in one sentence? Determine the maximum number of shashliks that can be cooked
# What category does this feel like? Feels like an array problem.
# What are the constraints telling me? 
# What's my first instinct? Go through array one by one
# Is there another approach?
# What's the gotcha / edge case? 

t = int(input())

for i in range(t):
    k,a,b,x,y = map(int, input().split())
    count = 0
    if x < y:
        while k >= a:
            count+=1
            k-=x
