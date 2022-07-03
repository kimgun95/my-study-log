def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    idx = 1
    dir = [[0,1], [0,-1], [1,0], [-1,0]] # 우, 좌, 하, 상
    di = 0
    if horizontal == True:
        di = 0
    else:
        di = 2

    def clean(y, x, size):
        nonlocal idx, di

        answer[y][x] = idx
        idx += 1

        ny, nx = y, x

        while True:
            if di == 0:
                if nx == size:
                    break
            elif di == 1:
                if nx == 0:
                    break
            elif di == 2:
                if ny == size:
                    break
            elif di == 3:
                if ny == 0:
                    break
            ny, nx = ny + dir[di][0], nx + dir[di][1]
            answer[ny][nx] = idx
            idx += 1
        if n % 2 != 0:
            if ny == 0 and nx == n - 1:
                print(ny, nx)
                return
        elif n % 2 == 0:
            if ny == n - 1 and nx == 0:
                return


        if di == 0: # 우측 이동
            if ny == 0: # down 이동
                di = 2
            else: # up
                di = 3
            clean(ny + dir[di][0], nx + dir[di][1], size)
        elif di == 2: # 아래 이동
            if nx == 0: # right 이동
                di = 0
            else: # left
                di = 1

            clean(ny + dir[di][0], nx + dir[di][1], size)
        elif di == 1:
            di = 2
            clean(ny + dir[di][0], nx + dir[di][1], size + 1)
        else:
            di = 0
            clean(ny + dir[di][0], nx + dir[di][1], size + 1)

        return

    clean(0, 0, 1)
    return answer

print(solution(4, True))
print(solution(5, False))