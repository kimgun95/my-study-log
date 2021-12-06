from typing import List


# 개어려운 문제, 아이디어 떠오르기 힘듬
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)):
            # 0이 나올수록 i에 빼줘야 할 cnt값이 커지는 격
            if nums[i] == 0:
                cnt += 1
            elif cnt > 0:
                nums[i - cnt], nums[i] = nums[i], 0
        return nums


s = Solution()
print(s.moveZeroes([0,1,0,3,12]))