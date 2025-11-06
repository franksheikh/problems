class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        ans = [-1] * n

        red_graph = {i:[] for i in range(n)}
        blue_graph = {i:[] for i in range(n)}

        for a,b in redEdges:
            red_graph[a].append(b)
        
        for x,y in blueEdges:
            blue_graph[x].append(y)
        
        q = collections.deque([
            # node, last_color, steps
            (0,'blue',0),
            (0,'red',0),
        ])

        seen = {
            (0,'blue'),
            (0,'red')
        }

        while q:
            node, last_color, steps = q.popleft()

            if ans[node] == -1:
                ans[node] = steps
            elif ans[node] > -1:
                ans[node] = min(steps, ans[node])

            # last color red, explore blue
            if last_color == 'red':
                for neighbor in blue_graph[node]:
                    if not (neighbor, 'blue') in seen:
                        seen.add((neighbor, 'blue'))
                        q.append((neighbor, 'blue', steps + 1))

            # last color blue, explore red
            elif last_color == 'blue':
                for neighbor in red_graph[node]:
                    if not (neighbor, 'red') in seen:
                        seen.add((neighbor, 'red'))
                        q.append((neighbor, 'red', steps + 1))
        
        return ans
                


            

            
        