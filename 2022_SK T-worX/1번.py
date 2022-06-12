# 유사 sort를 구현하는 문제
def solution(p):
    length = len(p)
    answer = [0 for _ in range(length)]
    for i in range(length):
        min_idx = i
        for j in range(i, length):
            if p[min_idx] > p[j]:
                min_idx = j
        if i != min_idx:
            temp = p[min_idx]
            p[min_idx] = p[i]
            p[i] = temp
            answer[i] += 1
            answer[min_idx] += 1

    return answer