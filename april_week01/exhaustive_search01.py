def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]
    for idx in range(0, len(answers)):
        if p1[idx % 5] == answers[idx]:
            count[0] += 1
        if p2[idx % 8] == answers[idx]:
            count[1] += 1
        if p3[idx % 10] == answers[idx]:
            count[2] += 1

    m = max(0, count[0])
    m = max(m, count[1])
    m = max(m, count[2])

    for i in range(0, len(count)):
        if count[i] == m:
            answer.append(i + 1)
    return answer


# 1, 2, 3 출력
print(solution([1,3,2,4,2]))