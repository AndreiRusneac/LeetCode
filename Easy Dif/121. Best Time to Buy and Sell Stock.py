from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))