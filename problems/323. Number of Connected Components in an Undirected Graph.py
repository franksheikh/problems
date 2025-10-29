'''

1. create a graph of N + E

{
    0: [1],
    1: [0,2]
    2: [1]
    3: [4]
    4: [3]
}

2. create a seen set
(

)

3. 
iterate from 0 to n:
    if i is not in seen:
        add i to seen
        dfs from i

4. dfs
    when we finish a dfs call, we will increment our cc (connected components)
    this is because we have exhausted all options via one route
    if we iterate again and encounter a new route, we will exit because
    it has already been seen
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        cc = 0
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                
        seen = set()

        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                cc += 1
        
        return cc
