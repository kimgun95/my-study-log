def solution(atmos):
    answer = 0
    cnt = 0
    for a, b in atmos:
        if a < 81 and b < 36:
            if cnt != 0:
                cnt += 1
        elif a >= 151 and b >= 76:
            if cnt == 0:
                answer += 1
            cnt = 0
            continue
        else:
            if cnt == 0:
                answer += 1
            cnt += 1
        if cnt == 3:
            cnt = 0

    return answer


print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))
print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]	))
print(solution([[30, 15], [80, 35]]))