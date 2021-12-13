# 해밍 웨이트: 사용 된 알파벳의 기호 0과 다른 기호의 수 (여기서는 1이 된다)
# 2가지 풀이법
# 1. n을 이진수로 변환 후 1의 개수 카운트
# 2. 이진수 n의 1을 하나씩 줄이는 방법: n & (n - 1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. 정말 쉬운 풀이
        # return bin(n).count('1')

        # 2. 비트에 대한 이해 필요: 루프때마다 마지막 1이 사라짐
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count