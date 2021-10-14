my_parent = {}
money = {}


def divide(seller, amount):
    if seller == "-":
        return
    up = amount // 10
    mine = amount - up
    money[seller] += mine
    # 1원 미만의 값이 나올 때는 재귀 종료. 이 코드 하나로 런타임 에러 케이스 해결
    if up < 1:
        return
    divide(my_parent[seller], up)
    return


def solution(enroll, referral, seller, amount):
    answer = []

    for i in range(1, len(enroll) + 1):
        index = i - 1
        my_parent[enroll[index]] = referral[index]

    for i in my_parent:
        money[i] = 0

    for i in range(len(seller)):
        divide(seller[i], amount[i] * 100)

    for i in enroll:
        answer.append(money[i])
    print(answer)
    return answer


e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
s = ["young", "john", "tod", "emily", "mary"]
a = [12, 4, 2, 5, 10]
solution(e, r, s, a)