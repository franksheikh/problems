class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        seen = set()
        shortest = +inf
        n = len(grid)
        q = collections.deque([
            ([0,0],1)
        ])

        while q:
            matrix, steps = q.popleft()
            row, col = matrix
            
            if (row,col) in seen:
                continue
            
            seen.add((row,col))

            if row >= n or col >= n or row < 0 or col < 0:
                continue

            if grid[row][col] == 1:
                continue

            if row == n - 1 and col == n - 1:
                # bfs -> guaranteed to find the shortest path
                return steps

            # down
            q.append(((row + 1, col),steps + 1))
            # up
            q.append(((row - 1, col),steps + 1))
            # right
            q.append(((row, col + 1),steps + 1))
            # left
            q.append(((row, col - 1),steps + 1))
            # down and to the right
            q.append(((row + 1, col + 1),steps + 1))
            # down and to the left
            q.append(((row + 1, col - 1),steps + 1))
            # up and to the right
            q.append(((row - 1, col + 1),steps + 1))
            # up and to the left
            q.append(((row - 1, col - 1),steps + 1))
        
        return -1
            
        