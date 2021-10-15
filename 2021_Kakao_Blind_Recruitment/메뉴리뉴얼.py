# 문제 이해가 안됐음. 동일 갯수의 메뉴구성은 최대값인 것만 추가할 수 있었음.
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    # 메뉴 구성 갯수에 따라 answer에 추가
    for c in course:
        arr = []
        for o in orders:
            # 메뉴를 정렬시킨 후 조합을 하면 정렬된 조합 값이 나옴
            comb = combinations(sorted(o), c)
            arr += comb
        arr_count = Counter(arr)
        # 조합이 된 메뉴들의 최대값이 1이 아니어야 추가할 수 있음
        if arr_count and max(arr_count.values()) != 1:
            for i in arr_count:
                if arr_count[i] == max(arr_count.values()):
                    answer += [''.join(i)]
    return sorted(answer)


o = ["XYZ", "XWY", "WXA"]
c = [2,3,4]
print(solution(o, c))