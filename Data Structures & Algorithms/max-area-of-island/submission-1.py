class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols):
                return 0

            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            count = 1

            for dr, dc in directions:
                count += dfs(r + dr, c + dc)

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea
