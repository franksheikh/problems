# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        seen = set()

        q = collections.deque([target])
        d = 0

        while q and d < k:
            n = len(q)
            for _ in range(n):
                node = q.popleft()

                if not node or node.val in seen:
                    continue
                
                seen.add(node.val)
                  
                for neighbor in [node.parent, node.left, node.right]:
                    if neighbor and neighbor.val not in seen:
                        q.append(neighbor)
            d += 1
        
        return [v.val for v in q]

# 1

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        seen = set()

        def dfs(node,parent):
            if not node:
                return
            
            node.parent = parent

            dfs(node.left, node)
            dfs(node.right,node)
        
        dfs(root, None)
        a = []

        q = collections.deque([target])
        d = 0

        while q and d < k:
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                seen.add(node.val)

                if d == k:
                    a.append(node.val)
                
                if node.parent and node.parent.val not in seen:
                    q.append(node.parent)
                if node.left and node.left.val not in seen:
                    q.append(node.left)
                if node.right and node.right.val not in seen:
                    q.append(node.right)
            d += 1
        
        return a

''' 
Optimized
'''


#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        seen = set([target])

        def dfs(node,parent):
            if not node:
                return
            
            node.parent = parent

            dfs(node.left, node)
            dfs(node.right,node)
        
        dfs(root, None)
        
        a = []

        q = collections.deque([target])
        d = 0

        while q and d < k:
            n = len(q)

            for _ in range(n):
                node = q.popleft()

                for neighbor in [node.left,node.right,node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)

            d += 1
        
        return [v.val for v in q]



        