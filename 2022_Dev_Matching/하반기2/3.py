# 이 문제를 해결 못한 이유
# 지하철 역은 앞, 뒤 역 모두 진행이 가능한데, 이렇게 진행을 시킬 경우 무한 루프가 만들어짐
# 그렇다고 방문 체크를 한다면 '빠르게 환승하여 목표지점을 도달하는 경우'가 '느리더라도 환승 없이 목표지점을 가는 경우'를 제치고 답이 될 수 있음
from collections import deque


def solution(subway, start, end):
    answer = 1e9
    for i in range(len(subway)):
        subway[i] = list(map(int, subway[i].split()))
    dict = {} # 어떤 역에 몇 호선이 있어!
    for i in range(len(subway)):
        for j in range(len(subway[i])):
            if subway[i][j] not in dict:
                dict[subway[i][j]] = [i]
            else:
                dict[subway[i][j]].append(i)
    print(subway)
    print(dict)


    def bfs(node): # node 는 역
        stack = deque([[node, 0, None, None]])
        while stack:
            cur, count, before, idx = stack.popleft()
            if cur == end:
                nonlocal answer
                answer = min(answer, count)
            if cur == start and before is not None:
                continue
            for line in dict[cur]: # line 은 호선
                if before is None or before != line: # 첫 역일 때 혹은 환승일 때
                    for i in range(len(subway[line])):
                        print(line, i)
                        if subway[line][i] == cur:
                            if before != line:
                                count += 1
                            if i+1 >= len(subway[line]):
                                stack.append([subway[line][0], count, line, 0])
                            else:
                                stack.append([subway[line][i+1], count, line, i+1])
                elif before == line: # 환승 아닐 때
                    if idx+1 >= len(subway[line]):
                        stack.append([subway[line][0],count,line,0])
                    else:
                        stack.append([subway[line][idx+1],count,line,idx+1])


    bfs(start)
    return answer



print(solution(["1 2 3 4 5 6 7 8", "2 11", "0 11 10", "3 17 19 12 13 9 14 15 10", "20 2 21"], 1, 9))
print(solution(["1 2 3 4 5 6 7 8 9 10", "2 8"], 1, 10))
print(solution(["0 1 2 3 4", "1 12 13 14"], 2, 12))