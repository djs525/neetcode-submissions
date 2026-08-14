class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        dxns = [[-1,0],
                [1,0],
                [0,1],
                [0,-1]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                
                r,c = q.popleft()
            
                for dr, dc in dxns:
                    row, col = r + dr, c + dc
                    #now we need to make sure that this place in the grid is within bounds and it is a non rotten orange spot. 
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1


        return time if fresh == 0 else -1






