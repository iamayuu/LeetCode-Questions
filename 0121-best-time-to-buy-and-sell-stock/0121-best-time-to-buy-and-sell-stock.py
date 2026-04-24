class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_buy_price = float("inf")
        max_profit = 0

        for crr_price in prices:
            min_buy_price = min(min_buy_price, crr_price)
            max_profit = max(max_profit, crr_price-min_buy_price)

        return max_profit