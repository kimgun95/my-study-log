input = [4, 6, 2, 9, 1]


def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array




selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!