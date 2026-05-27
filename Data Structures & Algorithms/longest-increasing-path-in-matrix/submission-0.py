class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Hashmap to store longest increasing path
        # at a certain coordinate (r, c) -> LIP
        dp = {}

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Need to pass in previous value to make sure 
        # path is increasing
        def dfs(r, c, prevValue):
            if (r < 0 or r >= rows or 
            c < 0 or c >= cols or matrix[r][c] <= prevValue):
                return 0
            
            if (r, c) in dp: 
                return dp[(r, c)]

            # Minimum longest path is always 1
            res = 1

            for x, y in directions:
                # Go through each direction and calculate the 
                # longest path
                res = max(res, 1 + dfs(r + x, c + y, matrix[r][c]))

            dp[(r, c)] = res
            return res

        # Perform this for every element in the grid
        for r in range(rows):
            for c in range(cols):
                # Default prevValue is -1 for the first iteration
                dfs(r, c, -1)

        # Get the max of our cached values
        return max(dp.values())

    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)


            
        
        