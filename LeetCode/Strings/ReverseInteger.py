class Solution:
    def reverse(self, x: int) -> int:
        # 1. 음수 체크
        minus = 1
        if x < 0:
            minus = -1
            x *= -1
        # 2. 숫자 reverse
        reverse_x = list(str(x))
        reverse_x.reverse()
        reverse_x = int(''.join(reverse_x))
        reverse_x *= minus
        # 3. reverse 값이 (-2^31, 2^31 - 1) 범위를 벗어나면 리턴 0
        if reverse_x < -pow(2, 31) or reverse_x >= pow(2, 31) or reverse_x == 0:
            return 0
        return reverse_x


s = Solution()
print(s.reverse(1534236469))
print(s.reverse(-123))