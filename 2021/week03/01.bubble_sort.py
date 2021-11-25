input = [4, 6, 2, 9, 1]

# 2중 for 문에서 안 쪽 for문을 수행할 때 마다 맨 마지막 숫자는 완벽히 정렬이 된다.
# 따라서 안 쪽 for문의 range는 진행될 수록 뒤 숫자까지 비교를 할 필요가 없기 때문에 -i를 통해 범위를 줄여 나간다.
# 하지만 시간 복잡도가 그렇다고 크게 주는 건 아니기에 O(N)의 시간 복잡도를 갖는다고 하는듯..?
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!