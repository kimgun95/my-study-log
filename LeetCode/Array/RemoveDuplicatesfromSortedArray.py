from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        length = len(nums)
        for i in range(length):
            if i == 0 or nums[i] != stack[-1]:
                stack.append(nums[i])
        answer = len(stack)
        for i in range(length):
            if i < answer:
                nums[i] = stack[i]
            else:
                nums[i] = ''
        return answer


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))