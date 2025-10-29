'''
Time - O(n) 
- At most, we visit every room once

Space - O(n)
- We build a graph with N nodes and, at most, N keys. So O(n + n) => O(n)

'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        graph = {room:[] for room in range(n)}
        seen = set()

        def dfs(room):
            for key in graph[room]:
                if key not in seen:
                    seen.add(key)
                    dfs(key)

        
        for i in range(n):
            room = rooms[i]
            for j in range(len(room)):
                graph[i].append(room[j])
        
        seen.add(0)
        dfs(0)

        return len(seen) == n


        
'''
More optimized
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set({0})

        def dfs(room):
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    dfs(key)

        seen.add(0)
        dfs(0)
                
        return len(seen) == n

        