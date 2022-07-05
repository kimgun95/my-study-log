def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    idx = 1
    dir = [[0,1], [1,0], [0,-1], [-1,0]] # 동남서북
    if horizontal:
        di = 0
    else:
        di = 1

    def clean(y, x, size):
        nonlocal idx, di
        ny, nx = y, x
        # 1. 직진할 수 있을 때 까지
        while 0 <= y <= size and 0 <= x <= size:
            answer[y][x] = idx
            idx += 1
            ny, nx = y, x
            y += dir[di][0]
            x += dir[di][1]
        # 2. size*size 크기 블럭을 채웠는지 확인
        for i in range(1, 4):
            d = (di + i) % 4
            dy, dx = ny + dir[d][0], nx + dir[d][1]
            if 0 <= dy <= size and 0 <= dx <= size and answer[dy][dx] == 0:
                di = d
                return clean(dy, dx, size)
        # 3. size*size 블럭을 모두 채웠으면 다음 크기를 채우기
        for i in range(1, 4):
            d = (di + i) % 4
            dy, dx = ny + dir[d][0], nx + dir[d][1]
            if 0 <= dy < n and 0 <= dx < n and answer[dy][dx] == 0:
                di = d
                return clean(dy, dx, size + 1)
        return

    clean(0, 0, 1)
    return answer


print(solution(4, True)) # 4*4 사이즈, 우측진행
print(solution(5, False)) # 5*5 사이즈, 아래진행