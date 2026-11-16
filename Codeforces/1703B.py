t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    
    set_s = set(s)
    
    print((len(set_s) *2)+ (len(s) - len(set_s)))