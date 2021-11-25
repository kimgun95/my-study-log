input_value = "hello my name is gunkim"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        # space 같은 공백이 있기 때문에 알파벳인지 확인 필요
        if 'a' <= i <= 'z':
            index = ord(i) - ord('a')
            alphabet_occurrence_array[index] += 1

    max_value = 0
    max_value_idx = 0
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > max_value:
            max_value = alphabet_occurrence_array[index]
            max_value_idx = index

    return chr(max_value_idx + 97)


result = find_max_occurred_alphabet(input_value)
print(result)