def rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    return 6


def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
           cnt += 1
        if i == 0:
            zero += 1
    answer.append(rank(cnt + zero))
    answer.append(rank(cnt))
    print(answer)
    return answer


l = [45, 4, 35, 20, 3, 9]
wn = [20, 9, 3, 45, 4, 35]
solution(l, wn)