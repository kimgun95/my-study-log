# 해밍 거리: 한 문자열을 다른 문자열로 변경하는 데 필요한 최소 대체 수
# 위 정의를 착안하여 x와 y가 서로 다른 지점이 몇 개인지 파악하는 게 중요 -> xor 연산 적합
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1. 내 풀이
        # return bin(x ^ y).count('1')
        # 2. 함수 사용 없는 풀이
        xor = x ^ y
        count = 0
        for _ in range(32):
            count += xor & 1
            xor = xor >> 1
        return count