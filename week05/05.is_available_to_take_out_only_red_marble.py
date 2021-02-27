from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 동, 서, 남, 북
# 이 아이디어는 잘 써먹어야 할듯
row = [0, 0, 1, -1]
col = [1, -1, 0, 0]


def move_until_wall_or_hole(r, c, direct_r, direct_c, game_map):
    move_count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while game_map[r + direct_r][c + direct_c] != "#" and game_map[r][c] != "O":
        r += direct_r
        c += direct_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    # 이동한 위치 저장
    queue = deque()
    n = len(game_map)
    m = len(game_map[0])
    # bfs를 위한 방문 위치 저장(4차원 배열)
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    r_r, r_c, b_r, b_c = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                r_r, r_c = i, j
            elif game_map[i][j] == "B":
                b_r, b_c = i, j
    visited[r_r][r_c][b_r][b_c] = True
    queue.append((r_r, r_c, b_r, b_c, 1))

    # queue에 저장한 위치들로부터 출구 찾아가기
    while queue:
        red_row, red_col, blue_row, blue_col, count = queue.popleft()
        # 10회 안에 탈출하지 못하면 break 및 False반환
        if count > 10:
            break

        # 각 위치에서 동, 서, 남, 북 4가지의 경우를 생각
        for i in range(4):
            # 두 개의 구슬을 이동
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, row[i], col[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, row[i], col[i], game_map)
            # 파랑구슬이 빠지면 continue
            if game_map[next_blue_row][next_blue_col] == "O":
                continue
            # 빨강구슬만 빠지면 True 반환
            elif game_map[next_red_row][next_red_col] == "O":
                return True
            # 두 구슬의 위치가 겹칠 때
            elif next_red_row == next_blue_row and next_red_col == next_blue_col:
                # 이동 방향이 많은 것이 다른 구슬 뒤에 있던 것
                if r_count > b_count:
                    next_red_row -= row[i]
                    next_red_col -= col[i]
                else:
                    next_blue_row -= row[i]
                    next_blue_col -= col[i]
            # 현재 위치가 방문하지 않았더라면 True로 visited에 저장 및 queue에 append
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, count + 1))

    return False

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
