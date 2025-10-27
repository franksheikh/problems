class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # y, x
        coords = [
            # up
            [-1,0],
            # down
            [1, 0],
            # left
            [0,-1],
            # right
            [0,1],
        ]
        def dfs(y,x):
            if y < 0 or y == len(grid):
                return
            if x < 0 or x == len(grid[0]):
                return
            if grid[y][x] == "0":
                return
            else:
                grid[y][x] = "0"
            
            for nY,nX in coords:
                dfs(y + nY, x + nX)
        
        c = 0
    
        # n
        for i in range(len(grid)):
            row = grid[i]
            # m
            for j in range(len(row)):
                if grid[i][j] == "1":
                    dfs(i,j)
                    c += 1
            
        
        return c

            

