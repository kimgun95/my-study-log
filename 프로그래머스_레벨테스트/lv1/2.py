# 주어진 숫자 n을 3진법으로 치환 후 뒤집기
# 뒤집은 수를 다시 10진법으로 치환 후 반환
def solution(n):
    answer = 0

    def recur(num):
        if num < 3:
            return num
        return recur(num // 3) * 10 + (num % 3)

    number = str(recur(n))
    for i in range(len(number)):
        answer += (3 ** i) * int(number[i])
    return answer