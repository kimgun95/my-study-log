def go_up(arr, x, y, x_minus, val, lst):
    if x < x_minus:
        return val
    tmp = arr[x][y]
    arr[x][y] = val
    lst.append(tmp)
    return go_up(arr, x - 1, y, x_minus, tmp, lst)


def go_left(arr, x, y, y_minus, val, lst):
    if y < y_minus:
        return val
    tmp = arr[x][y]
    arr[x][y] = val
    lst.append(tmp)
    return go_left(arr, x, y - 1, y_minus, tmp, lst)


def go_down(arr, x, y, x_plus, val, lst):
    if x > x_plus:
        return val
    tmp = arr[x][y]
    arr[x][y] = val
    lst.append(tmp)
    return go_down(arr, x + 1, y, x_plus, tmp, lst)


def go_right(arr, x, y, y_plus, val, lst):
    if y > y_plus:
        return val
    tmp = arr[x][y]
    arr[x][y] = val
    lst.append(tmp)
    return go_right(arr, x, y + 1, y_plus, tmp, lst)


def solution(rows, columns, queries):
    answer = []
    # 초기 리스트 생성
    num = 1
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    # 쿼리 명령 마다 회전 및 최솟값 추가
    for query in queries:
        # 첫 행/렬, 마지막 행/렬 정보를 저장
        x = query[0] - 1
        y = query[1] - 1
        x_plus = query[2] - 1
        y_plus = query[3] - 1
        # 회전 시작 (오른쪽, 아래, 왼쪽, 위 순서로 진행)
        val = arr[x][y]
        lst = []
        lst.append(val)
        val = go_right(arr, x, y + 1, y_plus, val, lst)
        val = go_down(arr, x + 1, y_plus, x_plus, val, lst)
        val = go_left(arr, x_plus, y_plus - 1, y, val, lst)
        val = go_up(arr, x_plus - 1, y, x, val, lst)
        answer.append(min(lst))
    print(answer)
    return answer


r = 100
c = 97
q = [[1,1,100,97]]
solution(r, c, q)