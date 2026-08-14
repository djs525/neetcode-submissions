class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogColor = image[sr][sc]
        newColor = color
        visited = set()

        ROWS = len(image)
        COLS = len(image[0])

        def dfs(r,c):

            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                image[r][c] != ogColor or
                (r,c) in visited):
                return 
            
            visited.add((r,c))
            image[r][c] = newColor
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            visited.remove((r,c))

        dfs(sr, sc)

        return image


