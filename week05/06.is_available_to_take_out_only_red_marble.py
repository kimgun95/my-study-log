import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    # 집과 치킨집의 갯수 체크를 통해 집, 치킨집의 위치 리스트 생성
    num_chi, num_house = 0, 0
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 2:
                num_chi += 1
            elif city_map[i][j] == 1:
                num_house += 1
    chicken_loc = [()] * num_chi
    house_loc = [()] * num_house

    # 집과 치킨집의 위치를 리스트에 저장
    loc_chi, loc_house = 0, 0
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 2:
                chicken_loc[loc_chi] = (i, j)
                loc_chi += 1
            elif city_map[i][j] == 1:
                house_loc[loc_house] = (i, j)
                loc_house += 1

    # 치킨집 위치 리스트를 combination을 통해 경우의 수 계산 및 리스트로 생성
    comb_list = list(itertools.combinations(chicken_loc, m))

    # 치킨 거리 최솟값
    result_min = sys.maxsize
    # 경우의 수를 모두 체크
    for c in comb_list:
        # 경우에 대한 치킨 거리 저장
        total_distance = 0
        # 모든 집에 대하여 체크
        for house in house_loc:
            min_distance = sys.maxsize
            # 집에서 어떤 치킨집이 가장 가까운지 체크
            for chicken in c:
                x, y = house
                a, b = chicken
                distance = abs(x - a) + abs(y - b)
                if distance < min_distance:
                    min_distance = distance
            total_distance += min_distance
        # 저장한 치킨거리의 최솟값을 확인
        if total_distance < result_min:
            result_min = total_distance

    return result_min


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
