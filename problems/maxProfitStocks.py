'''
[10,11,1,100]
max_profit
min = 1
max = -Infinity

curr_profit = 0 

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        min_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            curr = price - min_price
            max_profit = max(max_profit, curr)
            min_price = min(min_price, price)
        
        return max_profit






        