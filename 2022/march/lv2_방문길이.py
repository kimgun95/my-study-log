def go(direction):
    if direction == 'U':
        return [0, 1]
    elif direction == 'D':
        return [0, -1]
    elif direction == 'R':
        return [1, 0]
    else:
        return [-1, 0]


def solution(dirs):
    answer = 0
    save = []
    x, y = 0, 0
    for dir in dirs:
        go_x, go_y = go(dir)
        nx, ny = x + go_x, y + go_y
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if ([x, y, nx, ny] not in save) and ([nx, ny, x, y] not in save):
            answer += 1
            save.append([x, y, nx, ny])
        x, y = nx, ny
    return answer


print(solution("ULURRDLLU"))