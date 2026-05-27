"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Helper function to check the value of all items in a square
        # row, col = top-left corner of square
        # size = width/height of square
        def check(row, col, size):
            # Save the first value in this square
            start = grid[row][col]

            # Check if every value in this square is the same
            for r in range(row, row + size):
                for c in range(col, col + size):

                    # If another value is found, this square cannot be a leaf
                    if grid[r][c] != start:

                        # Split the square into 4 quarters
                        half = size // 2

                        # Recursively build each quadrant and the run the helper
                        topLeft = check(row, col, half)
                        topRight = check(row, col + half, half)
                        bottomLeft = check(row + half, col, half)
                        bottomRight = check(row + half, col + half, half)
                        
                        # Return a non-leaf node
                        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

            # If the loops are finished, this means that every value in the 
            # square was the same, so return a leaf node
            # start == 1 is True if all values in the square are 1, and False
            # if all values in the square are 0
            return Node(start == 1, True)

        # Start with the entire grid
        return check(0, 0, len(grid))


    # Time Complexity: O(n^2 log n) because height of tree is log n and
    # at worst case you could iterate through all values in the grid
    # so n^2, at each level of the tree
    # Space Complexity: O(log n) for the recursion stack
        