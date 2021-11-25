input_value = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_value = 0
    for i in array:
        if i > max_value:
            max_value = i
    return max_value


result = find_max_num(input_value)
print(result)