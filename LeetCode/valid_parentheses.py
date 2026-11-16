# if a bracket is at position 0, its counterpart would be at -1
# if a bracket is at position 1, its counterpart would be at -2
# if a bracket is at position 2, its counterpart would be at -3
# the relation is the first -(index+1)

s = input()
list_s = list(s)

correct = True


for i in range(len(list_s)):
        if list_s[i] == "(":
                if list_s[-(i+1)] != ")" and list_s[i+1] != ")":
                        correct = False
        if list_s[i] == "[":
                if list_s[-(i+1)] != "]" and list_s[i+1] != "]":
                        correct = False
        if list_s[i] == "{":
                if list_s[-(i+1)] != "}" and list_s[i+1] != "}":
                        correct = False

print(correct)