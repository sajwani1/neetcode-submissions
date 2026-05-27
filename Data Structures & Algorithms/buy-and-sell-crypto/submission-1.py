class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minval = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < minval:
                minval = prices[i - 1]
            
            profit = max(profit, prices[i] - minval)
        
        return profit

        