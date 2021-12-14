from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [*nums]
        dp[1] = max(dp[0], dp[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return max(dp)


s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))