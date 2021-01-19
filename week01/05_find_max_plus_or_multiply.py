input_value = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    cal_value = array[0]
    for i in range(1, len(array)):
        if 0 <= cal_value <= 1 or 0 <= array[i] <= 1:
            cal_value += array[i]
        else:
            cal_value *= array[i]
    return cal_value


result = find_max_plus_or_multiply(input_value)
print(result)