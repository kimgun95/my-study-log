def solution(grade):
    answer = 0
    length = len(grade)
    for i in range(length - 2, -1, -1):
        if grade[i] > grade[i + 1]:
            dif = grade[i] - grade[i + 1]
            answer += dif
            grade[i] -= dif

    return answer