number_of_layers = int(input())
result = ""

for i in range(number_of_layers):
    if i % 2 == 0:
        word = "hate"
    else:
        word = "love"
    
    if i < number_of_layers - 1:
        result += "I " + word + " that "
    else:
        result += "I " + word + " it"

print(result)