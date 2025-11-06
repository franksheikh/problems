# 1
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        start_row, start_col = entrance

        def is_valid(row,col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] != '+'
        
        def is_valid_exit(row,col):
            top_bound = 0
            bottom_bound = m - 1
            left_bound = 0
            right_bound = n - 1

            not_start = (row,col) != (start_row, start_col)
            # not_in_seen = (row,col) not in seen
            is_at_edge = (row == top_bound or row == bottom_bound or col == left_bound or col == right_bound)
            is_cell = maze[row][col] == '.'

            return not_start and is_at_edge and is_cell
        
        # if the entrance is a wall
        if not is_valid(start_row, start_col):
            return -1

        dirs = [
            # up
            [-1, 0],
            # down
            [1, 0],
            # right
            [0, 1],
            # left
            [0, -1]
        ]

        seen = {(start_row, start_col)}
        # row, col, steps
        q = collections.deque([(start_row, start_col,0)])

        # bfs, get to the exit in the minimum amount of steps possible
        while q:
            row, col, steps = q.popleft()
            print('row',row,'col',col, maze[row][col])

            if is_valid_exit(row,col):
                return steps
            
            for dY, dX in dirs:
                nY = row + dY
                nX = col + dX

                if (nY, nX) not in seen:
                    seen.add((nY, nX))
                    if is_valid(nY, nX):
                        q.append((nY, nX, steps + 1))

        return -1


# 2

