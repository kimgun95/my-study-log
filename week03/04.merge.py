array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    arr = []
    idx_a = idx_b = 0
    while idx_a < len(array1) and idx_b < len(array2):
        if array1[idx_a] < array2[idx_b]:
            arr.append(array1[idx_a])
            idx_a += 1
        else:
            arr.append(array2[idx_b])
            idx_b += 1
    if idx_a != len(array1):
        while idx_a < len(array1):
            arr.append(array1[idx_a])
            idx_a += 1
    if idx_b != len(array2):
        while idx_b < len(array2):
            arr.append(array2[idx_b])
            idx_b += 1
    return arr


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!