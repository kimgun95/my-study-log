import itertools
from math import sqrt


def is_demical(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    candidate = set()
    for i in range(len(numbers)):
        # 1. 순열로 모든 경우 리스트 제작
        # 2. int형으로 변환
        # 3. set형으로 데이터 변환(중복 제거)
        num = set(map(int, map(''.join, itertools.permutations(numbers, i+1))))
        # 합집합
        candidate |= num

    answer = 0
    candidate = list(candidate)
    for i in candidate:
        if is_demical(i):
            answer += 1

    return answer

# 11, 101로 2개가 답
print(solution("011"))

