# write functions to check palindrome and divisibilyt by 12
# create looop to determine solution
# 1125 == 5211

# t = int(input())

# for k in range(t):
#     n = int(input())

#     def palindrome(x):
#         original = x
#         new_x = 0

#         while x > 0:
#             new_x = new_x * 10 + x % 10
#             x = x // 10

#         return original == new_x
#     saved_i = 0
#     saved_j = 0
#     found = False
#     for i in range(0, n): #palindrome
#         for j in range(0, n): #divisible by 12
#             if j % 12 == 0 and palindrome(i):
#                 if j+i == n:
#                     found = True
#                     saved_i = i
#                     saved_j = j
#                     break
                    
    
#     if found:
#         print(f"{saved_i} {saved_j}")
#     else:
#         print(-1)


#issues wth time complexity
#take values of b, then check those values for a

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 10:
        print(-1)
    else:
        r = n % 12

        if r == 10:
            a = 22
        else:
            a = r

        b = n - a
        print(a, b)