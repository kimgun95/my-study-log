def solution(registered_list, new_id):
    answer = new_id
    word, num = '', ''
    if answer in registered_list:
        for i in range(len(answer)):
            if 'a' <= answer[-1] <= 'z':
                word = answer
                num = '1'
                break
            if answer[i] < 'a' or answer[i] > 'z':
                word = answer[0:i]
                num = answer[i:len(answer)]
                break

        number = int(num)
        answer = ''.join([word, num])
        while answer in registered_list:
            number += 1
            num = str(number)
            answer = ''.join([word, num])

    return answer


r = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
n = "cow"
print(solution(r, n))