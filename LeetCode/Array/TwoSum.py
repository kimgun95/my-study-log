from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) // 2 + 1):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))