# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

        while q:
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



        