import sys


def solution():
    INF = float('inf')
    N = int(input())
    VISITED_ALL = (1 << N) - 1

    # 마지막으로 방문한 도시, 그리고 그때의 visited 여부를 저장하는 배열
    # N개의 도시에 대해 2^N의 경우에 대한 visited를 만든다
    # 2^N 경우의 수가 비트마스킹을 이용한 (1 << N)으로 만들 수 있음. None로 초기화 함
    dp = [[None] * (1 << N) for _ in range(N)]

    cost_arr = []
    for i in range(N):
        arr = list(map(int, sys.stdin.readline().split()))
        cost_arr.append(arr)

    def dfs(last_city, visit):
        # 모두 방문했다면 처음으로 돌아오는 최종 간선 값 반환
        if visit == VISITED_ALL:
            if cost_arr[last_city][0] != 0:
                return cost_arr[last_city][0]
            return INF
        # 이전에 경로 계산을 한 적이 있었다면(dp에 존재) 저장된 값 반환
        if dp[last_city][visit] is not None:
            return dp[last_city][visit]
        # 처음 계산하는 경로라면 계산 시작
        cost = INF
        for city in range(N):
            if (1 << city) & visit == 0 and cost_arr[last_city][city] != 0:
                cost = min(cost, dfs(city, (1 << city) | visit) + cost_arr[last_city][city])
        # dp에 위에서 계산한 경로를 저장한다
        dp[last_city][visit] = cost
        # last_city와 visit를 통해 계산한 cost를 반환
        return cost

    # 첫 번째 도시 시작, 첫 번째 도시만 방문했다는 비트마스크
    answer = dfs(0, 1 << 0)
    return answer


print(solution())