def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n + 1)]
    for p in paths:
        graph[p[0]].append([p[1], p[2]])
        graph[p[1]].append([p[0], p[2]])
    answer = [-1, float('inf')]

    def bfs(start, now, isTop, distance):
        nonlocal answer, visit
        if visit[now] == 1 or distance > answer[1]:
            return
        visit[now] = 1
        if now in summits: # 산봉우리
            if isTop != -1:
                return
            isTop = now
            visit = [0] * (n + 1)
            visit[now] = 1
        if now in gates: # 출입구
            if distance != 0:
                if now == start and isTop != -1:
                    answer = [isTop, distance]
                return
        for go in graph[now]:
            bfs(start, go[0], isTop, max(distance, go[1]))

    for g in gates:
        visit = [0] * (n + 1)
        bfs(g, g, -1, 0)

    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))