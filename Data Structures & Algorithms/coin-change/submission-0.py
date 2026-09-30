class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # memo[0] ... memo[amount]
        memo = {}

        # run dfs on each recursive problem
        def dfs(amount):
            # if we are at 0, this is our base case
            if amount == 0:
                return 0
            # if we have already solved this value before,
            # get the min amount from the cache
            if amount in memo:
                return memo[amount]

            res = 1e99

            # go through all the possible coin options we have
            # because we have len(coins) number of decisions to make
            for c in coins:
                # subtract this coin from the amount
                if amount - c >= 0:
                    # take the minimum of our current result
                    # and the path of taking this coin 
                    res = min(res, 1 + dfs(amount - c))

            # add this new min value to the cache
            memo[amount] = res
            return res

        # if we have not updated res, this means that reaching
        # this amount with our coins is not possible, so return -1
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e99 else minCoins

        # Time Complexity: O(n * t) where n is the amount and t
        # is the number of coins, because at each value from 0-amount
        # we have to try all t coins
        # Space Complexity: O(t) because our cache will store 
        # the min number of coins for each value 0-amount
