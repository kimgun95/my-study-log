# 십진수 맨 뒤에 숫자를 하나씩 추가할 때 num = (num * 10) + x 하는 것처럼 푸는 것
# answer를 << 1 하는 것은 비트를 왼쪽으로 밀어주는 것, 그럼 맨 우측 비트가 0으로 빌 것
# 맨 우측 비트는 n의 맨 우측 비트를 가져오면 됨, 1과 &연산을 하면 간단히 가져올 수 있음
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans