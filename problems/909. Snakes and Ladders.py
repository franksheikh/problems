class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def convert_cell(square):
            row = (n - 1) - ((square - 1) // n)
            col = (square - 1) % n

            # when we need to go right to left
            # if n is odd, n - 1 row is even
                # if last row even, then col is the same (left to right), no need to change
            # if n is even, n - 1 row is odd
                # if last row is odd, then col is the same (left to right), no need to change
            
            # for the n - 2 row, we need to alternate. but that row could be odd OR even, so row
            # is not enough to use to determine

            # N - 2
                # N = 6
                    # 6 - 1 - 4 = 1
                # N = 5
                    # 5 - 1 - 3 = 1
            # N - 3
                # N = 6
                    # 6 - 1 - 3 = 2
                # N = 5
                    # 5 - 1 - 2 = 2
            
            # start counting from the bottom row
            if ((n - 1) - row) % 2:
                col = (n - 1) - col
            
            return (row, col)

        seen = set()
        q = collections.deque([(1, 0)])  # (square, steps)

        while q:
            square, steps = q.popleft()

            if square == n * n:
                return steps

            for i in range(1,7):
                next_cell = square + i
                row,col = convert_cell(next_cell)
                
                if 1 <= next_cell <= n * n:
                    if board[row][col] != -1:
                        next_cell = board[row][col]
                    if next_cell not in seen:
                        seen.add(next_cell)
                        q.append((next_cell, steps + 1))

        return -1