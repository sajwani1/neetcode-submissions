class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The max number for bananas per hour will be the
        # largest number in the array
        l, r = 1, max(piles)
        res = r

        # Use binary search to go through a list from
        # 1 to the largest number and find the minimum
        # rate that works best
        while l <= r:
            k = (l + r) // 2 # middle 

            totalTime = 0
            for p in piles:
                # Hours it takes to finish a pile
                # is number of bananas divided by rate
                totalTime += math.ceil(float(p) / k)
            # If this time is less than the hour limit,
            # try binary search on the left side to see
            # if a smaller rate can be tried
            if totalTime <= h:
                res = k 
                r = k - 1
            # Otherwise, try binary search on the right side
            # if the rate is too small
            else:
                l = k + 1
        return res

        # Time Complexity: O(n * log m)
        # Space Complexity: O(1)