array = [5, 3, 2, 1, 6, 8, 7, 4]

# log_2 n 의 시간 복잡도를 갖는다
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_arr = merge_sort(array[:mid])
    right_arr = merge_sort(array[mid:])
    return merge(left_arr, right_arr)

# len(array1) + len(array2) 의 크기만큼 비교를 하기 때문에 O(N)의 시간 복잡도를 갖는다.
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


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!