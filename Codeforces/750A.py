n, k = map(int, input().split())
time_left = 240 - k
total_time = 0
solved = 0

for i in range(1, n+1):
    total_time += 5*i
    
    if total_time <= time_left:
        solved +=1
    else:
        break
print(solved)