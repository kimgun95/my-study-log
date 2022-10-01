from collections import deque

def solution(maps):
    answer = {}
    n, m = len(maps), len(maps[0])
    visit = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != '.':
                if maps[i][j] not in answer:
                    answer[maps[i][j]] = 1
                else:
                    answer[maps[i][j]] += 1
    dir = [[1,0], [-1,0], [0,1], [0,-1]]

    def bfs(y, x):
        dq = deque([[y, x]])
        visit[y][x] = True
        country = {}
        country[maps[y][x]] = 1
        while dq:
            sy, sx = dq.popleft()
            for dy, dx in dir:
                ny, nx = sy + dy, sx + dx
                if 0<=ny<n and 0<=nx<m and maps[ny][nx] != '.' and visit[ny][nx] is False:
                    visit[ny][nx] = True
                    dq.append([ny, nx])
                    if maps[ny][nx] not in country:
                        country[maps[ny][nx]] = 1
                    else:
                        country[maps[ny][nx]] += 1
        return country

    def war(co):
        max_value = max(co.values())
        max_alpha = ''
        for c in co:
            if co[c] == max_value and c >= max_alpha:
                max_alpha = c
        for c in co:
            if co[c] < max_value and c != max_alpha:
                answer[max_alpha] += co[c]
                answer[c] -= co[c]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != '.' and visit[i][j] is False:
                c = bfs(i, j)
                war(c)

    return max(answer.values())


print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))
print(solution(["XY..", "YX..", "..YX", ".AXY"]))