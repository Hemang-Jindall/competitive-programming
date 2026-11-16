t = int(input())

for i in range(t):
    array_length, number_of_operations, maximum_value = map(int, input().split())

    original_array = list(map(int, input().split()))

    copy_array = original_array.copy()
    for i in range(number_of_operations):
        index, added_number = map(int, input().split())
        index = index -1
        copy_array[index] += added_number
        if copy_array[index] > maximum_value:
            copy_array = original_array.copy()
    print(*copy_array)       
        