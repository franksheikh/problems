'''
Time - O(n)
- this is because we iterate over the connections a max of 3n times. once for creating the edges, once for creating the graph, and another as we do recursive depth first searches, where linear is preserved because we use a set to avoid traversing over nodes we have already visited

Space - O(n + m)
- this is because we create a graph of n nodes with m connections each
- m = n - 1 roads
- O (n + n - 1) = O(n)

'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        c = 0
        edges = {(a,b) for a,b in connections}
        graph = {city:[] for city in range(n)}

        for city, neighbor in connections:
            graph[city].append(neighbor)
            graph[neighbor].append(city)

        seen = set()
        def dfs(city):
            nonlocal edges, graph, seen, c

            for neighbor in graph[city]:
                if neighbor not in seen:
                    if not (neighbor, city) in edges:
                        c += 1
                    seen.add(neighbor)
                    dfs(neighbor)
        seen.add(0)
        dfs(0)
        return c
        