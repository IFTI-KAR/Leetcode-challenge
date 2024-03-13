# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price=i
            current_profit=i-min_price
            if current_profit>max_profit:
                max_profit =current_profit
        return max_profit
        
