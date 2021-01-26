finding_target = 17
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    min_value = 0
    max_value = len(array) - 1
    guess = (min_value + max_value) // 2
    while min_value <= max_value:
        if target == array[guess]:
            return True
        elif target < array[guess]:
            max_value = guess - 1
        else:
            min_value = guess + 1
        guess = (min_value + max_value) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)