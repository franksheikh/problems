'''

1. iterate: 
    if (row,col) is in our seen, continue
    go until we find a starting node with value 1
2. do a dfs starting from grid[row][col] in the up, right, left, down dxns
    - start with 1 as a counter
3. add each position to a seen set, as a tuple (row, col)
4. DFS call:
- check for bounds
- use coordinate system
- When we encounter a new position with a 1, call dfs with an incremented counter, and recurse again

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        area = 0
        n = len(grid)
        m = len(grid[0])

        coords = [
            [-1, 0], # going up
            [1, 0],  # going down
            [0, 1],  # going right
            [0, -1]  # going left
        ]

        def dfs(y, x):
            nonlocal area, coords, n, m, seen

            if y < 0 or y >= n or x < 0 or x >= m:
                return 0

            if (y,x) in seen:
                return 0 

            
            # at this point, we have checked repeats vs boundaries

            seen.add((y,x))

            if grid[y][x] == 0:
                return 0
            
            # continue looking through rest of adjacent nodmes

            curr = 0
            
            for a, b in coords:
                nY = a + y
                nX = b + x
                curr += dfs(nY, nX)

            area = max(curr,area)
            return curr + 1
            
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen:
                    if grid[i][j] == 0:
                        seen.add((i,j))
                        continue
                    if grid[i][j] == 1:
                        curr = dfs(i, j)
                        area = max(area, curr)

        return area
