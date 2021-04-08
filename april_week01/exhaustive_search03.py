def solution(brown, yellow):
    answer = []
    tile_cnt = brown + yellow
    for a in range(tile_cnt - 1, 2, -1):
        if tile_cnt % a == 0:
            b = int(tile_cnt / a)
            if (a - 2) * (b - 2) == yellow and a * b == brown + yellow and a >= b:
                answer = [a, b]
    return answer


# [24, 3] 이 출력된다.
print(solution(50, 22))