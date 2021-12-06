from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False


s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))