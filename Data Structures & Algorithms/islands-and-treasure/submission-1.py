class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Queue to check the different cells and perform bfs
        q = deque()

        # Dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # Visited set to ensure nothing is visited twice
        visit = set()

        # Helper function to verify the cell we have moved to
        # is valid
        def addCell(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols 
            or (r, c) in visit or grid[r][c] == -1):
                return
        
            # Add this land cell to the visited set and add it 
            # onto the queue to determine what layer
            visit.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                # If the cell is a treasure cell, we want
                # to start the bfs from here, so add these
                # coordinated to the queue
                if grid[r][c] == 0:
                    q.append([r, c])
                    # Also don't forget to add to the visit set
                    visit.add((r, c))

        # Start the distance from 0, this will increase for
        # every layer 
        dist = 0
        
        while q:
            # Go through the queue and keep popping elements
            for i in range(len(q)):
                r, c = q.popleft()

                # Update the value in the cell with its
                # distance from treasure
                grid[r][c] = dist

                # Iterate over the neighbors of the current cell
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            # Increase dist because we are on the next layer
            dist += 1
        
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)


        


        