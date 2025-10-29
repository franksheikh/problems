# Optimal
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degrees = [0] * n
        for _, y in edges:
            in_degrees[y] += 1
        
        return [i for i in range(n) if in_degrees[i] == 0]

# My Solution (unoptimized)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        values = {i for i in range(0,n)}

        for a,b in edges:
            graph[a].append(b)
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor in values:
                    values.remove(neighbor)
                    dfs(neighbor)
        
        for i in range(n):
            if i in values:
                dfs(i)
        
        return list(values)