from itertools import combinations
import math


def isPrime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


def solution(nums):
    comb = list(combinations(nums, 3))
    answer = 0
    s = set()
    for c in comb:
        total = sum(c)
        if total in s:
            answer += 1
            continue
        if isPrime(total):
            answer += 1
            s.add(total)
    return answer


print(solution([1,2,7,6,4]))