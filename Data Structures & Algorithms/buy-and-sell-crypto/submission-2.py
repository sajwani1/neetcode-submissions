class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Store smallest value in array
        minval = prices[0]
        profit = 0

        # i represents the selling point, so it starts at 1
        for i in range(1, len(prices)):
            # If the value before i is smaller than the previous 
            # minimum value, update it
            if prices[i - 1] < minval:
                minval = prices[i - 1]
            
            # profit becomes the max because the previous profit
            # and the new calculated one
            profit = max(profit, prices[i] - minval)
        
        return profit

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        