#MEX is the smallest non negative integer not present in an array
#0 to k-1 elements should be present, k shouldn't be present,
#n: length of array
#k: MEX value to be made

'''t = int(input())

for i in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    operations = 0

    if k == 0:
        operations +=1
        print(f"if: {operations}")
        
    else:
        for i in range(0, max(n,k)):
            if arr[i] != i and arr[i] != k:
                arr[i] = i
                operations += 1
                print(f"else, {i}: {operations}")
    for i in arr:
        if i == k:
            operations += 1
            print(f"for: {operations}")'''


# do not need to modify the array
# count the numbers from 0 to k-1 not present
# count the number of Ks present
# take max of the two counts
# understand time complexity of this solution

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = [0] * (n + 1)

    for x in arr:
        freq[x] += 1

    count_1 = 0

    for x in range(k):
        if freq[x] == 0:
            count_1 += 1

    count_2 = freq[k]

    print(max(count_1, count_2))