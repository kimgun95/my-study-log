# 런타임 에러, 틀렸습니다 둘 다 나오는데 이유를 모르겠음
from collections import deque


def solution(worldmap):
    answer = float('inf')
    print(worldmap)
    # 동, 동남, 남, 남서, 서, 서북, 북, 북동
    direct = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    n, m = len(worldmap), len(worldmap[0])
    visit = [[False]*m for _ in range(n)]

    def bfs(y,x):
        dq = deque([[y,x,0,0]])
        visit[y][x] = True
        while dq:
            sy, sx, dir, time = dq.popleft()
            if sy == n-1 and sx == m-1:
                nonlocal answer
                answer = time
                break
            for i in [-1,0,1]:
                nDir = (dir + i + 8) % 8
                dy, dx = sy+direct[nDir][0], sx+direct[nDir][1]
                if 0<=dy<n and 0<=dx<m and worldmap[dy][dx] == '.' and visit[dy][dx] == False:
                    if nDir == 1:
                        if worldmap[dy][dx-1] == 'X' or worldmap[dy-1][dx] == 'X':
                            continue
                    elif nDir == 3:
                        if worldmap[dy][dx+1] == 'X' or worldmap[dy-1][dx] == 'X':
                            continue
                    elif nDir == 5:
                        if worldmap[dy][dx+1] == 'X' or worldmap[dy+1][dx] == 'X':
                            continue
                    elif nDir == 7:
                        if worldmap[dy][dx-1] == 'X' or worldmap[dy+1][dx] == 'X':
                            continue
                    visit[dy][dx] = True
                    dq.append([dy,dx,nDir,time+1])
    bfs(0,0)
    return answer



print(solution(["..XXX", "..XXX", "...XX", "X....", "XXX.."]))
print(solution([".....", "XXX..", "XXXX.", "XXXX."]))