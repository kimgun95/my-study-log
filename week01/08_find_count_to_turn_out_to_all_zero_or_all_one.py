input_val = "010101010000010101010101"


# 연속된 0과 1의 개수가 몇개인지 계산 후 최솟값을 반환
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    continuous_zero = 0
    continuous_one = 0
    for i in range(0, len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i] == '0':
                continuous_zero += 1
            else:
                continuous_one += 1
    if string[len(string) - 1] == '0':
        continuous_zero += 1
    else:
        continuous_one += 1
    return min(continuous_zero, continuous_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input_val)
print(result)