'''
If the grid has a size of n times n, this algorithm has a time complexity of O of n^2 - there are n^2 elements and each element is iterated over twice initially (once for the row it occupies and once for the column it occupies). 

Populating and then iterating over the hash maps will be dominated by this. 

The space complexity is O of n^2 - if all rows and columns are unique, then each of the two hash maps will both grow to a size of n, with each key having a length of n.

TKWY:
- Identify solution before coding
- Use naive/simplest approach first.
'''
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

        
        
        