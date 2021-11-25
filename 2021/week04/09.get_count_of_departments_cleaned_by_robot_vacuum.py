current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    room_map[r][c] = 2
    # 사방이 벽이거나 청소를 했을 때
    if room_map[r][c - 1] and room_map[r - 1][c] and room_map[r + 1][c] and room_map[r][c + 1]:
        # 뒤가 벽일 때
        if (d == 0 and room_map[r + 1][c] == 1) or (d == 1 and room_map[r][c - 1] == 1) or (d == 2 and room_map[r - 1][c] == 1) or (d == 3 and room_map[r][c + 1] == 1):
            count = 0
            for i in room_map:
                for j in i:
                    if j == 2:
                        count += 1
            return count
        # 뒤가 벽이 아니라면 후진
        if d == 0:
            return get_count_of_departments_cleaned_by_robot_vacuum(r + 1, c, d, room_map)
        elif d == 1:
            return get_count_of_departments_cleaned_by_robot_vacuum(r, c - 1, d, room_map)
        elif d == 2:
            return get_count_of_departments_cleaned_by_robot_vacuum(r - 1, c, d, room_map)
        else:
            return get_count_of_departments_cleaned_by_robot_vacuum(r, c + 1, d, room_map)
    # 주변에 청소 공간이 있을 남아 있을 때
    if d == 0:
        if room_map[r][c - 1] == 0:
            return get_count_of_departments_cleaned_by_robot_vacuum(r, c - 1, 3, room_map)
        return get_count_of_departments_cleaned_by_robot_vacuum(r, c, 3, room_map)
    elif d == 1:
        if room_map[r - 1][c] == 0:
            return get_count_of_departments_cleaned_by_robot_vacuum(r - 1, c, 0, room_map)
        return get_count_of_departments_cleaned_by_robot_vacuum(r, c, 0, room_map)
    elif d == 2:
        if room_map[r][c + 1] == 0:
            return get_count_of_departments_cleaned_by_robot_vacuum(r, c + 1, 1, room_map)
        return get_count_of_departments_cleaned_by_robot_vacuum(r, c, 1, room_map)
    else:
        if room_map[r + 1][c] == 0:
            return get_count_of_departments_cleaned_by_robot_vacuum(r + 1, c, 2, room_map)
        return get_count_of_departments_cleaned_by_robot_vacuum(r, c, 2, room_map)



# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
