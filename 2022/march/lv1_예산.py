def solution(d, budget):
    d.sort()
    answer = 0
    for cost in d:
        budget -= cost
        if budget < 0:
            break
        answer += 1
    return answer


print(solution([2,2,3,3], 10))