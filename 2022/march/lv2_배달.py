import heapq


def dijkstra(start_node, size, go):
    heap = []
    dp = [float('inf')] * (size + 1)
    dp[start_node] = 0
    heapq.heappush(heap, [start_node, 0])
    while heap:
        cur_node, cur_weight = heapq.heappop(heap)
        if dp[cur_node] < cur_weight:
            continue
        for moved_node, weight in go[cur_node]:
            total_weight = cur_weight + weight
            if dp[moved_node] > total_weight:
                dp[moved_node] = total_weight
                heapq.heappush(heap, [moved_node, total_weight])
    return dp


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, time in road:
        graph[a].append([b, time])
        graph[b].append([a, time])
    answer = 0
    d = dijkstra(1, N, graph)
    for cost in range(1, N + 1):
        if d[cost] <= K:
            answer += 1
    return answer


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))