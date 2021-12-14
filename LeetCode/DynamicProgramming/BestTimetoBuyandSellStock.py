# min_price 사용하는 아이디어를 생각 못함
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, profit = float('inf'), 0
        for price in prices:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        return profit