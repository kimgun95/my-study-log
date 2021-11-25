import sys


def solution():
    N = int(input())
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # dp 생성 및 초기값 설정
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = cost[0]

    # 현재 선택한 색일 때 최솟값 = 이전에 현재 색과 다른 색을 선택한 것의 최솟값 + 현재 선택 비용
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
    return min(dp[N - 1])


print(solution())