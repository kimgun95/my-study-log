from typing import List


# Biweekly Contest 67: 5934 ~ 5937 번 문제들
# 이 문제는 통과
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new_nums = sorted(nums)
        stack = {}
        for i in range(k):
            if new_nums[len(new_nums) - 1 - i] in stack:
                stack[new_nums[len(new_nums) - 1 - i]] += 1
            else:
                stack[new_nums[len(new_nums) - 1 - i]] = 1
        new_nums = []
        for i in range(len(nums)):
            if nums[i] in stack and stack[nums[i]] > 0:
                new_nums.append(nums[i])
                stack[nums[i]] -= 1

        return new_nums


s = Solution()
print(s.maxSubsequence([2,1,3,3], 2))