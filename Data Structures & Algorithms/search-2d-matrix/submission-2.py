class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            row = (top + bot)//2

            
            #if the row's first element is greater than target, bot = row - 1
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
            
        if not top <= bot:
            return False
        
        l = 0
        r = COLS - 1

        while l <= r:
            mid = (l + r)//2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False