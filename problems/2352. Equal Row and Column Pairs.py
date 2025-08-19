class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        max_n = 0
        hmr = defaultdict(int)
        hmc = defaultdict(int)
        n = len(grid)

        # horizontally
        i = 0
        while i < n:
            hoz = grid[i]
            ver = []
            j = 0
            while j < n:
                ver.append(grid[j][i])
                j += 1
            
            hoz_key = str(hoz)
            ver_key = str(ver)

            hmr[hoz_key] += 1
            hmc[ver_key] += 1
            i += 1
        
        o = 0
        for key in hmr:
            o += hmr[key] * hmc[key]

        return o

        
        
        