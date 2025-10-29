'''

edges:
[
    [0,1],
    [1,2],
    [2,0]
]


seen set

1. create graph of {node: vertices}

{
    0: [1,2]
    1: []
    2: []
}

2. dfs(source)
    - if our neighbor not in seen (prevent repeats):
        - if current node == destination, reassign found to true

call dfs(source)

3. default case return found (initialized to false)

'''

# Approach 1 DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        graph = {i:[] for i in range(n)}
        for ui, vi in edges:
            graph[ui].append(vi)
            graph[vi].append(ui)
        
        def dfs(node):
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False
        seen.add(source)
        return dfs(source)
        

# Approach 2 BFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = [0] * n 
        graph = {i:[] for i in range(n)}
        
        for from_node, to_node in edges:
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)
        
        q = collections.deque({source})
        seen[source] += 1

        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            neighbors = graph[node]
            nl = len(neighbors)

            for i in range(nl):
                neighbor = neighbors[i]
                
                if not seen[neighbor]:
                    seen[neighbor] += 1
                    q.append(neighbor)
            
        return False
