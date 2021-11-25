input_val = "abaeabacd"


def find_not_repeating_character(string):
    arr = [0] * 26
    nrc_arr = []
    # 알파벳이 몇 번 쓰였는지 배열에 저장
    for idx in range(0, len(string)):
        index = ord(string[idx]) - ord('a')
        arr[index] += 1
    # 1번 쓰인 알파벳을 따로 배열에 저장
    for i in range(0, 26):
        if arr[i] == 1:
            nrc_arr.append(chr(i + 97))
    # string의 첫 문자부터 nrc_arr에 해당 문자가 있는지 체크
    for ch in string:
        if ch in nrc_arr:
            return ch
    return '_'


result = find_not_repeating_character(input_val)
print(result)