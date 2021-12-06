from typing import List


# in-place하게 수정을 하는데 아이디어가 떠오르지 않음
# 다른 분의 깔끔한 3줄 풀이법으로 이해함
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # k값 설정을 nums의 길이에 맞게 수정
        k = k % len(nums)
        # 1. 전체 배열을 reverse
        reverse(0, len(nums) - 1)
        # 2. 앞에서 k개를 reverse
        reverse(0, k - 1)
        # 3. 나머지 부분 reverse
        reverse(k, len(nums) - 1)
        return


s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))