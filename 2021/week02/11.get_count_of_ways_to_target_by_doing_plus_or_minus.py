numbers = [2, 3, 1]
target_number = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    index = 0
    sum_val = 0
    cnt = 0
    result = []

    get_all_ways_to_plus_and_minus(array, index, sum_val, result)
    for i in result:
        if i == target:
            cnt += 1
    # print(result)
    return cnt


def get_all_ways_to_plus_and_minus(array, index, sum_val, result):
    if index == len(array):
        result.append(sum_val)
        return
    get_all_ways_to_plus_and_minus(array, index + 1, sum_val + array[index], result)
    get_all_ways_to_plus_and_minus(array, index + 1, sum_val - array[index], result)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))

