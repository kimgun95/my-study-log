from collections import deque


def solution(n, recipes, orders):
    r, o = {}, deque()
    # 요리의 조리 시간은 딕셔너리로 저장
    for i in range(len(recipes)):
        key, val = recipes[i].split()
        r[key] = int(val)
    # 주문되는 요리는 순서대로 리스트에 저장
    for i in range(len(orders)):
        lst = orders[i].split()
        o.append([lst[0], int(lst[1])])

    time = 0
    count = 0 # 마지막 음식인지 판단
    waiting = deque() # 시간 때 마다 주문되는 음식 순서대로 저장
    fire = [0] * n # 화구

    while True:
        time += 1
        # 1. 대기 음식 추가
        if o and o[0][1] == time:
            waiting.append(o.popleft())
        for i in range(n):
            # 2. 요리중인 음식 -1초
            if fire[i] != 0:
                fire[i] -= 1
            # 3. 빈 화구에 조리 시작
            if fire[i] == 0 and waiting:
                fire[i] = r[waiting[0][0]]
                count += 1
                # 4. 마지막 음식이라면 리턴
                if count == len(orders):
                    return time + fire[i]
                waiting.popleft()


print(solution(2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"]))
print(solution(3, ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"], ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]))
print(solution(1, ["COOKIE 10000"], ["COOKIE 300000"]))