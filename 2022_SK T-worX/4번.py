# 내가 생각하기에 energy에 값이 계속 더해지는 것이 문제가 있었던 것 같음
# 어차피 최대가 k이기 때문에 energy의 최대를 조정했어야 했음
def solution(grid, k):
    end_y, end_x = len(grid) - 1, len(grid[0]) - 1
    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and i != end_y and j != end_x:
                answer += 1
    visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dir = [[1,0], [-1,0], [0,1], [0,-1]]


    def dfs(y, x, energy, count):
        nonlocal answer
        if count >= answer: # 야영 횟수 백트래킹
            return
        if energy < 0: # 에너지 음수면 경로 실패
            return
        if y == end_y and x == end_x: # 도착지 오면 답 갱신 해보기
            answer = min(answer, count)
            return
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= end_y and 0 <= nx <= end_x and grid[ny][nx] != '#':
                visit[ny][nx] = 1
                if grid[ny][nx] == '.':
                    dfs(ny, nx, energy + k - 1, count + 1)
                dfs(ny, nx, energy - 1, count)
                visit[ny][nx] = 0
        return

    visit[0][0] = 1
    dfs(0, 0, k, 0)
    return answer