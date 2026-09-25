class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        dxns = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        def bfs(r,c):
            q = collections.deque()

            q.append([r,c])

            while q:
                r,c = q.popleft()

                for dr, dc in dxns:
                    row = r + dr
                    col = c + dc

                    if (row in range(ROWS) and
                        col in range(COLS) and
                        grid[row][col] == "1"):
                        q.append([row, col])
                        grid[row][col] = "0"

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands