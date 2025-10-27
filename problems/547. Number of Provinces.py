'''

Time - O(n + e (edges)) -> O(n), no, O(nxn) to build the hash map from an adjacency matrix
- We always iterated over the entire matrix to build the graph.
Space - O(n + e). 
- Hash map only grows if the edges actually exist.

'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        seen = set()
        c = 0

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
                    

        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                c += 1
        
        return c
