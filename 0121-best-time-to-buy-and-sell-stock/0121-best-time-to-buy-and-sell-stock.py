class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = 0

        for price in reversed(prices):
            if price > max_price:
                max_price = price
            elif max_price - price > max_profit:
                max_profit = max_price - price

        return max_profit