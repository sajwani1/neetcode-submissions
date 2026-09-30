class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        dp = {} # (r, c) -> LIP

        # dfs takes in current cell and prev value
        def dfs(r, c, prev):
            # check if new coordinates are out of bounds
            # or the value is not increasing
            if (r >= rows or r < 0 or c >= cols or c < 0 or 
                matrix[r][c] <= prev):
                return 0

            # if the LIP has already been calculated for this
            # cell, get the value from the cache
            if (r, c) in dp:
                return dp[(r, c)]

            # start the count with 1 because a path has to be
            # length 1 by default
            res = 1

            # compute the max LIP by adding 1 for this cell, 
            # and comparing to all neighbors of this cell, 
            # and adding on their already calculated path 
            # if in the cache
            res = max(res, 
                      1 + dfs(r + 1, c, matrix[r][c]),
                      1 + dfs(r - 1, c, matrix[r][c]), 
                      1 + dfs(r, c + 1, matrix[r][c]),
                      1 + dfs(r, c - 1, matrix[r][c]))
            
            # add the calculated LIP for this cell to the cache
            dp[(r, c)] = res
            
            return res  

        # go through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # start the prev value off at -1 since
                # no cell can have this value
                dfs(r, c, -1)

        # return the max of all stored paths 
        return max(dp.values())

        # Time Complexity: O(m * n) since we have to visit every
        # cell in the matrix, but once a cell has been visited,
        # their work becomes O(1) because it comes from the cache
        # Space Complexity: O(m * n) to store the entire cache matrix
                

        
        