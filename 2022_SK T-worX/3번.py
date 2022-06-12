# 단순 구현 문제
# 고민해 볼 법한 것: ①이 쓰여진 곳에서 선형탐색이 아닌 이분탐색을 통해 시간복잡도를 줄였어야 했나
# -> 입력값의 크기에 따라 필요 유무가 결정된다.
def solution(n, plans, clients):
    answer = [0 for _ in range(len(clients))]
    fee_money = [] # 요금제 금액
    fee_service = [[0 for _ in range(n + 1)] for _ in range(len(plans))] # 요금제 부가서비스
    for i in range(len(plans)): # 요금제 정리
        a = list(map(int, plans[i].split()))
        fee_money.append(a[0])
        if i != 0: # 이전 요금제의 부가서비스 목록을 deepcopy로 가져옴
            fee_service[i] = fee_service[i - 1][:]
        for val in a[1:]: # 부가서비스를 index로 접근하여 체크
            fee_service[i][val] = 1

    for i in range(len(clients)): # 손님 수 만큼 반복
        a = list(map(int, clients[i].split()))
        money = a[0]
        service = a[1:]
        for j in range(len(plans)): # ①
            enter = 0
            flag = -1
            if money <= fee_money[j]:
                enter = 1
                for val in service:
                    if fee_service[j][val] != 1:
                        flag = 0
            if enter == 1 and flag == -1:
                answer[i] = j + 1
                break

    return answer