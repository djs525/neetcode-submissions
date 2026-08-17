class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #here again, we are dealing with finding duplicates
        #sets are the best option
        #but hashSets!
        #we need 3, one for row traversal, one for col traversal,
        #one for the entire square itself
        
        rows = defaultdict(set) #row : set
        cols = defaultdict(set) #col : set
        squares = defaultdict(set) #square : set


        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == ".": continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True