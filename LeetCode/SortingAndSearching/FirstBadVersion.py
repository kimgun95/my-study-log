# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# 그냥 1부터 n까지 탐색을 하면 '시간초과'가 발생 -> 시간을 줄여야 함
# 이분탐색을 채용
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binarySearch(left, right):
            # 정답인 지점을 찾았더라도 binarySearch를 왼쪽으로 더 할 것이다.
            # 왼쪽 탐색 후 다시 오른쪽 탐색을 하는데 left 값은 정답 값으로 되며 right 값은 left보다 작은 값이 될 것
            # 따라서 이때! left를 리턴하면 됨
            if left > right:
                return left
            # mid 값은 left를 더하는 것을 주의!
            mid = left + (right - left) // 2
            if isBadVersion(mid) is False:
                return binarySearch(mid + 1, right)
            else:
                return binarySearch(left, mid - 1)

        return binarySearch(1, n)