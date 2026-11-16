s = str(input())

lower_case_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z']
upper_case_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
lower_count = 0
upper_count = 0

for i in s:
    if i in lower_case_list:
        lower_count += 1
    elif i in upper_case_list:
        upper_count += 1

if lower_count >= upper_count:
    print(s.lower())
else:
    print(s.upper())