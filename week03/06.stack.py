top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(array):
    arr = [0] * len(array)
    while array:
        height = array.pop()
        for i in range(len(array) - 1, -1, -1):
            if array[i] >= height:
                arr[len(array)] = i + 1
                break
    return arr


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!