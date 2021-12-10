class Solution(object):
    def isPowerOfThree(self, n):
        # 3^19는 최대 int 범위보다 작은 구간에서의 3의 최고 거듭수이다
        # 진짜 코딩문제가 아니라 수학문제 아닌가요???
        return n > 0 and pow(3, 19) % n == 0


s = Solution()
print(s.isPowerOfThree(27))