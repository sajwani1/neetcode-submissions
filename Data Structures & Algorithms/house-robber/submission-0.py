class Solution:
    def rob(self, nums: List[int]) -> int:
        # Just have to store the previous 2 values
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1, ...]
        # Can either rob the sum of rob1 and n, or rob2
        # n cannot be included with rob2 since it is next to it
        for n in nums:
            temp = max(n + rob1, rob2) 
            # rob1 moves down the line
            rob1 = rob2
            # rob2 becomes the new max
            rob2 = temp
        
        # By the time we reach the end, rob2 will be the max
        return rob2

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        

        