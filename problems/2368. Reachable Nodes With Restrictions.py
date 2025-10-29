class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        if not edges:
            return 1
        # create "restricted" set to check while traversing
        # count "restricted" nodes as already "seen"
        seen = {node for node in restricted}
        # need a graph
        graph = {node:[] for node in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # track our counts
        c = 1
        
        def dfs(node):
            nonlocal c
            for neighbor in graph[node]:
                if not neighbor in seen:
                    seen.add(neighbor)
                    c += 1
                    dfs(neighbor)
        
        # start with 0, root node
        seen.add(0)
        dfs(0)
        return c
        


        
        