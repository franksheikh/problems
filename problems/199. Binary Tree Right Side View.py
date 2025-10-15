'''
1
2 ->

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([(root, 1)])
        seen = set()
        o = []

        if not root:
            return o

        while q:
            n = len(q)
            for _ in range(n):
                node, level = q.popleft()
                if not level in seen:
                    o.append(node.val)
                    seen.add(level)
                if node.right:
                    q.append((node.right, level + 1))
                if node.left:
                    q.append((node.left, level + 1))

        return o
    

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        o = []

        if not root:
            return o

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                # iterate to the right most element of the current level
                if i == n - 1:
                    o.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return o


