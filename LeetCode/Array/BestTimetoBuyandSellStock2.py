from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                answer += prices[i] - prices[i - 1]
        return answer


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))