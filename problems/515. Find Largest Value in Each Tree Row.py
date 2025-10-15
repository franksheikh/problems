# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        o = []
        if not root:
            return o
        
        q = collections.deque([root])

        while q:
            n = len(q)
            local_max = -inf
            for i in range(n):
                node = q.popleft()
                local_max = max(local_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            o.append(local_max)
        return o
                
        