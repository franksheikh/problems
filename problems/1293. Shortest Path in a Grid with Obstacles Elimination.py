class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(row,col):
            return 0 <= row < n and 0 <= col < m
        n = len(grid)
        m = len(grid[0])
        obstacles = 1 if grid[0][0] == 1 else 0

        # row, col, obstacles encountered, current steps
        q = collections.deque([(0,0,obstacles,0)])

        # row, col, current_obstacles. same path can be used, but different number of
        # obstacles seen
        seen = {(0,0,obstacles)}

        dirs = [
            [0,-1],
            [0,1],
            [1,0],
            [-1,0]
        ]

        while q:
            row, col, current_obstacles, current_steps = q.popleft()

            if row == n - 1 and col == m - 1:
                return current_steps
            
            for dY, dX in dirs:
                nX = col + dX
                nY = row + dY
                obstacle_count = current_obstacles
                is_valid_next = valid(nY, nX)
                if is_valid_next and grid[nY][nX] == 1:
                    obstacle_count += 1
                if obstacle_count > k:
                    continue
                if not (nY, nX, obstacle_count) in seen and is_valid_next:
                    seen.add((nY, nX, obstacle_count))
                    q.append((nY, nX, obstacle_count, current_steps + 1))
        
        return -1



        