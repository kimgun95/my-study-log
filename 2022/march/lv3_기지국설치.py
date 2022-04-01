# 내 풀이는 시간초과가 발생했다. O(n)으로 해결했어야 했는데 그렇지 못함
# 전파가 닿지 않는 곳을 좀만 쉽게 생각해서 구해야 한다
# 추가로 math.ceil() 에 대해도 알게 되었다.
import math


def solution(n, stations, w):
    answer = 0
    distance = []
    for idx in range(1, len(stations)): # 기지국 사이 닿지 않는 구간 계산
        distance.append(stations[idx] - (stations[idx - 1] + 1 + 2 * w))
    distance.append(stations[0] - (w + 1)) # 맨 앞 구간 계산
    distance.append(n - (stations[-1] + w)) # 맨 뒤 구간 계산

    for d in distance:
        answer += math.ceil(d / (w * 2 + 1))
    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
