# Solution 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        local_min = inf
        if not root:
            return 0
        
        def dfs(node, depth=0):
            nonlocal local_min
            if not node:
                return 0
            depth += 1
            if not node.left and not node.right:
                local_min=min(local_min, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root)
        return local_min


# Solution 2
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If one subtree is empty, return the depth of the other
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Both subtrees exist, return minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))