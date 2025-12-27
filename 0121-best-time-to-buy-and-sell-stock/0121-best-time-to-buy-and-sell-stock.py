class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #Solution1 (Brute Force)
        # profit = 0
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i,len(prices)):
        #         profit = prices[j]-prices[i]
        #         if profit>max_profit:
        #             max_profit = profit
        # return max_profit

        #Solution 2 (Storing minimum buy price)
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p<min_price:
                min_price=p
            elif p-min_price>max_profit:
                max_profit=p-min_price
        return max_profit