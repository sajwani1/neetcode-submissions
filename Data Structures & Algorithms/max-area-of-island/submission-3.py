class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        # Store dimensions of grid
        rows = len(grid)
        cols = len(grid[0])

        # Create visited list to store nodes that have been seen
        visited = set()
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        # Create dfs to loop through each time you reach a "1" cell
        def dfs(r, c):
            # Don't add to the length of island if we go out of bounds
            if (r < 0 or c < 0 or r >= rows or c >= cols):
                return 0

            # Don't add to the length of island if we reach a "0" cell
            # or if it has already been visited
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            # Otherwise, add the element to the visited set
            visited.add((r, c))

            # Start count with 1 to represent the current island
            count = 1

            # Perform dfs in all 4 directions to see if we can add 
            # to the island
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)

            return count

        # Go through the entire grid
        for r in range(rows):
            for c in range(cols):
                # When we reach a "1", dfs through its
                # neighbors to see if there are more unvisited 1's
                if grid[r][c] == 1 and (r, c) not in visited:
                    # Update max area if necessary
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea

        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)

