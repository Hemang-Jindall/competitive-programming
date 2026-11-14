t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        print("1 1")
        #forgot to go to the next test case after printing
    if len(set(arr)) == len(arr):
        print(f"1 " + str(len(arr)))

    dict = {}
    
    for i in arr:
        dict[i] = dict.get(i,0) + 1

    #check which key has the most instances, had to look up the code for this

    highest_key = max(dict, key=dict.get)

    #used a python taken variable
    len = 0

    while len <=1:
        #used incorrect syntax of loop iteration
        for x in arr:
            if x == highest_key:
                print(f"{x}" + " ")
                len +=1
    
