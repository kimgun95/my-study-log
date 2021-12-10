import math


# 에라토스테네스의 체를 활용해야 '시간초과'를 면한다;;
# 단순 반복문을 활용하여 배수인 값을 false로 일일히 바꾸는 과정은 '시간초과'를 유발...
# 리스트 slice를 활용해서 시간을 단축시킨다
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        # 1. 각 숫자가 '소수'인지 판단하기 위한 자료 초기화
        primes = [True] * n
        primes[0] = primes[1] = False
        # 2. number의 제곱근 까지만 판별을 해줘도 모든 수에 대한 판별을 할 수 있음
        for i in range(2, int(math.sqrt(n)) + 1):
            # 3. 소수의 배수 값들을 모두 false로 바꾸는 과정
            if primes[i] is True:
                # 4. 이때 list slicing을 잘 활용, [start:end:step] 으로 생각
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        # 5. True의 개수 반환
        return sum(primes)


s = Solution()
print(s.countPrimes(10))