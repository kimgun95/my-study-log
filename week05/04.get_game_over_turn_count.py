from collections import deque

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 말의 정보: 행, 렬, 이동 방향(0:동, 1:서, 2:북, 3:남)

# 동 서 북 남
# →, ←, ↑, ↓
row = [0, 0, -1, 1]
column = [1, -1, 0, 0]


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    count = 0
    save = [[deque() for i in range(len(game_map))] for j in range(len(game_map))]
    # 말들을 해당 위치 큐에 저장
    for i in range(horse_count):
        save[horse_location_and_directions[i][0]][horse_location_and_directions[i][1]].append(i)

    while count <= 1000:
        for i in range(horse_count):
            orientation = horse_location_and_directions[i][2]
            check = 1
            # 말들이 밖 or 파랑을 만났을 때 처리
            if ((not 0 <= horse_location_and_directions[i][0] + row[orientation] < len(game_map)) or
                    (not 0 <= horse_location_and_directions[i][1] + column[orientation] < len(game_map)) or
                    (chess_map[horse_location_and_directions[i][0] + row[orientation]][horse_location_and_directions[i][1] + column[orientation]] == 2)):
                # 우선 방향 변경
                if orientation == 0:
                    orientation = 1
                elif orientation == 1:
                    orientation = 0
                elif orientation == 2:
                    orientation = 3
                else:
                    orientation = 2
                # 변경 후 또 만난다면 체크
                if ((not 0 <= horse_location_and_directions[i][0] + row[orientation] < len(game_map)) or
                        (not 0 <= horse_location_and_directions[i][1] + column[orientation] < len(game_map)) or
                        (chess_map[horse_location_and_directions[i][0] + row[orientation]][
                             horse_location_and_directions[i][1] + column[orientation]] == 2)):
                    check = 0
                horse_location_and_directions[i][2] = orientation
            # 체크가 변동 없는 곳은 이동 시작
            if check == 1:
                # 흰색으로 이동시
                if chess_map[horse_location_and_directions[i][0] + row[orientation]][
                             horse_location_and_directions[i][1] + column[orientation]] == 0:
                    save_remain = deque()
                    pop_check = 0
                    while save[horse_location_and_directions[i][0]][horse_location_and_directions[i][1]]:
                        pop_num = save[horse_location_and_directions[i][0]][horse_location_and_directions[i][1]].popleft()
                        if pop_num == i or pop_check == 1:
                            save[horse_location_and_directions[i][0] + row[orientation]][
                                horse_location_and_directions[i][1] + column[orientation]].append(pop_num)
                            pop_check = 1
                        save_remain.append(pop_num)
                    save[horse_location_and_directions[i][0]][horse_location_and_directions[i][1]] = save_remain
                # 빨강으로 이동시
                else:
                    while save[horse_location_and_directions[i][0]][horse_location_and_directions[i][1]]:
                        pop_num = save[horse_location_and_directions[i][0]][
                            horse_location_and_directions[i][1]].pop()
                        save[horse_location_and_directions[i][0] + row[orientation]][
                            horse_location_and_directions[i][1] + column[orientation]].append(pop_num)
                        if pop_num == i:
                            break
        for i in range(len(game_map)):
            for j in range(len(game_map)):
                if len(save[i][j]) == len(game_map):
                    return count
        count += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
