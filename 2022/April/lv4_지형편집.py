def solution(land, P, Q): # 추가P, 제거Q
    land2 = []
    for l in land:
        land2.extend(l)
    land2.sort()
    N = len(land2)
    cost = (sum(land2) - land2[0] * N) * Q # 최하층 생성
    answer = cost

    for i in range(1, N):
        if land2[i] != land2[i - 1]: # 새로운 층을 생성해야 한다면
            dif = land2[i] - land2[i - 1]
            cost += (dif * i * P) - (dif * (N - i) * Q)
            if answer < cost:
                break
            answer = cost
    return answer


print(solution([[1, 2], [2, 3]], 3, 2))
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))