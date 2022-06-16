from collections import deque


def solution(cacheSize, cities):
    answer = 0

    LRU = deque([])
    for city in cities: # 데이터 삽입
        c = city.upper()
        flag = -1
        for idx in range(len(LRU)): # 캐시에 데이터가 존재하는지 확인
            if LRU[idx] == c:
                flag = idx
                break
        if flag == -1: # 데이터가 없다면 cache miss
            LRU.appendleft(c)
            answer += 5
            if len(LRU) > cacheSize:
                LRU.pop()
        else: # 데이터가 있다면 cache hit
            del LRU[flag]
            LRU.appendleft(c)
            answer += 1
    return answer