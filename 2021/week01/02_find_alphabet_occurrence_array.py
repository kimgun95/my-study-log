def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        # space 같은 공백이 있기 때문에 알파벳인지 확인 필요
        if 'a' <= i <= 'z':
            index = ord(i) - ord('a')
            alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is gunkim"))