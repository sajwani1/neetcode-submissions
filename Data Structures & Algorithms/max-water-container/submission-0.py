class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Start the left pointer at the start and the right
        # pointer at the end
        l = 0
        r = len(heights) - 1

        maxWater = 0

        while l < r:
            # Calculate the area of the water between these
            # 2 pointers by multiplying length times width
            waterArea = (r - l) * min(heights[l], heights[r])
            # Update the maxWater variable if necessary
            maxWater = max(maxWater, waterArea)
            
            # Move the smaller height since a larger
            # height can increase the water area because
            # the smaller height is used for the area calculations
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater

        # Time Complexity: O(n) since the array is traversed once
        # Space Complexity: O(1) since only the area and the 
        # pointers are stored in memory


        