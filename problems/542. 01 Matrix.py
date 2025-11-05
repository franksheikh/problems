class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row,col):
            return 0 <= row < n and 0 <= col < m

        m = len(mat[0])
        n = len(mat)

        seen = set()
        q = collections.deque()

        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    seen.add((row,col))
                    q.append((row,col,1))
        
        dirs = [
            (0,-1),
            (0,1),
            (1,0),
            (-1,0)
        ]
        while q:
            row, col, steps = q.popleft()
            
            for dy, dx in dirs:
                nY = row + dy
                nX = col + dx
                
                # if nY, nX not in seen, we know it is a 1,
                # since we already added all the 0s
                if valid(nY, nX) and (nY, nX) not in seen:
                    seen.add((nY, nX))
                    q.append((
                        nY,
                        nX,
                        steps + 1
                    ))
                    mat[nY][nX] = steps
        
               
        return mat


