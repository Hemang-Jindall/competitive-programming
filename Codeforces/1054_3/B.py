# form pairs that minimise the sum of all |x-y|
# find the minimum value of the maximum difference that will be obtained
# sort the array, calculate differences, save the maximum

t = int(input())

for i in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    curr = 0
    max = 0
    i = 0
    arr.sort()

    while i < n-1:
        curr = arr[i+1] - arr[i]   
        if curr > max:
            max = curr
        i += 2

    print(max)

#don't shadow built ins such as max
#could have used for i in range(0,n,2):
#could have omitted curr: max_diff = max(mix_diff, arr[i+1]-arr[i])


t = int(input())

for i in range(t):
    
    n = int(input())
    arr = list(map(int, input().split()))
    max_diff = 0

    arr.sort()

    for i in range(0, n, 2):
        max_diff = max(max_diff, arr[i+1]-arr[i])
    
    print(max_diff)