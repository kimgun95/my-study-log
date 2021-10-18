from collections import Counter


def grade(sco):
    if sco >= 90:
        return 'A'
    elif sco >= 80:
        return 'B'
    elif sco >= 70:
        return 'C'
    elif sco >= 50:
        return 'D'
    return 'F'


def solution(scores):
    answer = []
    length = len(scores)
    # 평가자 개인 점수 리스트화
    person_score = [[] for _ in range(length)]
    value = []
    for j in range(length):
        for i in range(length):
            person_score[j].append(scores[i][j])
            if i == j:
                value.append(scores[i][j])
    # 유일한 최고점/ 유일한 최저점 확인
    for i in range(length):
        a = Counter(person_score[i])
        if value[i] == max(person_score[i]) and a[value[i]] == 1:
            del person_score[i][i]
        elif value[i] == min(person_score[i]) and a[value[i]] == 1:
            del person_score[i][i]
    # 평균 계산
    for i in range(length):
        answer.append(sum(person_score[i]) / len(person_score[i]))
    # 학점 계산
    for i in range(length):
        answer[i] = grade(answer[i])
    return ''.join(answer)


s = [[70,49,90],[68,50,38],[73,31,100]]
print(solution(s))