t = int(input())

for i in range(t):
    n = int(input())

    a = list(input())
    b = list(input())

    ans = "yes"
    
    for i in range(n-1):
        if a[i] == "(" and a[i+1] == "(":
            if b[i] == "(" and b[i+1] == "(":
                continue
            if b[i] == "(" and b[i+1] == ")":
                continue
            if b[i] == ")" and b[i+1] == ")":
                ans = "no"
                break
            if b[i] == ")" and b[i+1] == "(":
                ans = "no"
                break
        elif a[i] == "(" and a[i+1] == ")":
