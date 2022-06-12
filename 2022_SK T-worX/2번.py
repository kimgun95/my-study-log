# 단순 구현 문제
def solution(periods, payments, estimates):
    answer = [0, 0]

    def isVIP(date, money):
        if money >= 600000:
            if date >= 60:
                return "VIP"
            elif date >= 24 and money >= 900000:
                return "VIP"
        return None

    for i in range(len(periods)): # 인원수만큼 반복
        join_date = periods[i]
        cur_money = sum(payments[i])
        before = after = None
        before = isVIP(join_date, cur_money) # 이번 달 회원 등급 체크
        join_date += 1
        cur_money = cur_money - payments[i][0] + estimates[i]
        after = isVIP(join_date, cur_money)

        if before == "VIP" and after is None:
            answer[1] += 1
        elif before is None and after == "VIP":
            answer[0] += 1

    return answer