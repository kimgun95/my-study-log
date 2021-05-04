# 단지에 각자 다른 번호를 주는 것은 문제 해결과는 관련 없음
import sys
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 단지 내 아파트 수 카운트
num = 0
N = int(input( ))
s = [0 for i in range(N)]
visited = [[0] * N for _ in range(N)]
# s에는 아파트 유무(1, 0) 저장
for i in range(N):
    s[i] = (list(map(int, sys.stdin.readline().strip())))


# 아파트가 존재하고 방문하지 않았던 곳을 dfs 탐색
# 탐색시 방문 표시 및 아파트가 존재하면 num 카운트
def dfs(i, j):
    global num
    visited[i][j] = 1
    if s[i][j] == 1:
        num += 1
    for a in range(4):
        x = i + dx[a]
        y = j + dy[a]
        # s 리스트 범위를 벗어나서 탐색하지 않게 범위 조건 설정
        if 0 <= x < N and 0 <= y < N:
            if s[x][y] == 1 and visited[x][y] == 0:
                dfs(x, y)


def attach_number():
    num_list = []
    global num
    for i in range(N):
        for j in range(N):
            if s[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                num_list.append(num)
                num = 0
    print(len(num_list))
    for i in sorted(num_list):
        print(i)


attach_number()