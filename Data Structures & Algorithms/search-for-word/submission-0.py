class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # get dimensions of the board
        rows = len(board)
        cols = len(board[0])

        # create the dfs function because when
        # we see a letter that is part of the word, 
        # we want to go down that entire path to see
        # if the whole word is there

        # pass in r, c = current cell in grid, and i for 
        # current pos in word 
        def dfs(r, c, i):
            # if we have found all letters of the word, 
            # return true
            if i == len(word):
                return True

            # if the new cell we are evaluating is out of bounds,
            # already been visited, or doesn't match the
            # letter we are looking for, stop checking this path
            if (r < 0 or r > rows - 1 or 
                c < 0 or c > cols - 1 or
                board[r][c] == "#" or
                board[r][c] != word[i]):
                return False

            # otherwise, mark this cell as visited with a '#'
            board[r][c] = '#'

            # run the dfs algo on all 4 neighbors of this cell
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))

            # backtrack and restore the cell back to its
            # original character
            board[r][c] = word[i]
            return res

        # run dfs from every cell in the board, and start
        # off with i = 0 
        # if any paths return true, we have found the word
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

    # Time Complexity: O(m * n * 4^l) where m is the number 
    # of cells in the board and l is the length of the word
    # because we have to go through the entire grid, and then
    # we call the dfs helper 4 times for each letter of the word
    # Space Complexity: O(l) because for each letter of the word
    # we have to make a call to the recursion stack

         



        