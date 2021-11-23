# 마이너스 부호 뒤 모든 숫자는 빼주면 된다
def solution():
    # 1. 마이너스 기준으로 수식을 분리한다
    math_express = list(input().split('-'))
    # 2. 플러스가 있는 수식은 더하여 처리한다
    for i in range(len(math_express)):
        express = list(map(int, math_express[i].split('+')))
        if len(express) != 1:
            num = 0
            for j in range(len(express)):
                num += express[j]
            math_express[i] = num
    # 3. split으로 분리해 남아있는 문자열을 int형으로 변환
    math_express = list(map(int, math_express))
    # 4. 첫 숫자에서 그 뒤 숫자들은 모두 빼준다
    answer = math_express[0]
    for i in range(1, len(math_express)):
        answer -= math_express[i]
    return answer


print(solution())