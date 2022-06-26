from collections import deque


def solution(m, people, pairs):
    lang = {}
    peo = {}
    visited = {}
    for p in people:
        case = list(p.split()) # 사람, 사용가능 언어들
        for i in range(1, len(case)): # 사람 dict 생성
            if case[0] not in peo:
                peo[case[0]] = [int(case[i])]
            else:
                peo[case[0]].append(int(case[i]))
            if int(case[i]) not in lang: # 언어 dict 생성
                lang[int(case[i])] = [case[0]]
            else:
                lang[int(case[i])].append(case[0])
        visited[case[0]] = False # 해당 사람을 탐색했는지 체크하는 용도

    def bfs(start, end):
        nonlocal visited
        queue = deque([[start, -1]]) # 시작 사람, 시작 depth

        while queue:
            who, depth = queue.popleft()
            if who == end:
                return depth
            visited[who] = True
            for know_language in peo[who]: # 이 사람이 아는 언어
                for know_person in lang[know_language]: # 이 언어를 아는 사람
                    if visited[know_person] is False:
                        queue.append([know_person, depth + 1])
        return -1

    answer = []
    for i in range(len(pairs)):
        name = list(pairs[i].split())
        answer.append(bfs(name[0], name[1]))

    return answer


print(solution(9, ["A 1 2", "B 2 3 4", "C 4 5", "D 5 6 7", "E 6 7 8", "F 8 9"], ["A B", "C F"])) # [0, 2]
print(solution(9, ["A 1 2", "B 4 9", "C 4 5", "D 5 6 7", "E 6 7 8", "F 8 9"], ["A B", "C F"])) # [-1, 1]