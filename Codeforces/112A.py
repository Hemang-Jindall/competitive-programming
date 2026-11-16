string1 = input().lower()
string2 = input().lower()

shorter = ""

if len(string1) > len(string2):
    shorter = string2
else:
    shorter = string1

result = 0
    
for i in range(len(shorter)):
    if string1[i] == string2[i]:
        continue
    elif string1[i] > string2[i]:
        result = 1
        break
    elif string1[i] < string2[i]:        
        result = -1
        break

else:
    if len(string1) > len(string2):
        result = 1
    elif len(string1) < len(string2):
        result = -1

print(result)
        

    