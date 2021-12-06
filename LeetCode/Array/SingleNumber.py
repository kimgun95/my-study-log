from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        INF = float('inf')
        # 'use only constant extra space'를 만족하기 위해 temp만 만들어 사용
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = INF
            if temp not in nums:
                return temp
            nums[i] = temp


s = Solution()
print(s.singleNumber([2,2,1]))