# 이전 문제로 TSP문제를 풀고와서인지 dp, dfs에 심취해 있었다
# 그러나 결과는 '시간초과'만 초래할 뿐 이었다
import sys


def solution():
    N = int(input())
    time_table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 예외를 고려한 정렬
    # 만약 (2, 2), (1, 2) 순서로 회의 시간이 입려된다면 회의종료 -> 회의시작 순서로 정렬을 해야 탐색이 제대로 된다
    time_table.sort(key=lambda x: (x[1], x[0]))

    count = 1
    end_time = time_table[0][1]
    for i in range(1, N):
        if end_time <= time_table[i][0]:
            count += 1
            end_time = time_table[i][1]

    return count


print(solution())