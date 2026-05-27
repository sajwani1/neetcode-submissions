class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islandCount = 0
        # Get number of rows and columns from grid size
        rows = len(grid)
        cols = len(grid[0])

        # Establish the 4 directions we can move to once we
        # are at a cell- up, down, left, right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            # Ensure we are not stepping out of bounds
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                grid[r][c] == "0"):
                return
            
            # If the cell is a "1", turn it to a "0" to 
            # mark it as visited
            grid[r][c] = "0"
            
            # Apply the dfs in all directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Go through the entire grid
        for r in range(rows):
            for c in range(cols):
                # When we encounter a "1", dfs through
                # all its neighbors to see if it is connected
                # to more "1"s
                if grid[r][c] == "1":
                    dfs(r, c)
                    # Increase island count after going
                    # through the entire path for this island
                    islandCount += 1

        return islandCount

        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
  

                
            
        