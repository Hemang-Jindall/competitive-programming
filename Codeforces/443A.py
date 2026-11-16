input_string = str(input())
input_set = set()

for i in input_string:
    if i.isalpha():
        input_set.add(i)
print(len(input_set))