class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = set()
        nums = set(nums)
        for i in range(len(nums) + 1):
            answer.add(i)
        return list(answer - nums)[0]
        # 더 최적화한 풀이
        # n = len(nums)
        # return ((n * (n + 1)) // 2) - sum(nums)