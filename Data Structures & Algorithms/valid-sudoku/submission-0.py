class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # defaultdict initializes every key with an empty set
        # Create a set for each column, row, and square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        # key = (r//3, c//3) because with integer division,
        # this creates a 3x3 grid of squares that 9 boxes
        # fit in each
        squares = collections.defaultdict(set) 

        # Iterate through the entire board
        for r in range(9):
            for c in range(9):
                # If the box is empty, skip over it
                if board[r][c] == ".":
                    continue
                
                # If the number exists already in the set of numbers
                # created specifically for the row, col, or square
                # that box belongs to, this means it is a duplicate
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    
                    return False

                # If the number was seen for the first time, 
                # add it to the set for its corresponding 
                # col, row, and square
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
            
        return True


        