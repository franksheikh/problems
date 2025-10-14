# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Naive
class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        local_max = 0
        def traverse(node):
            nonlocal local_max
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            local_max = max(local_max,left + 1, right + 1)
            return 1 + max(left,right)
        traverse(root)
        return local_max

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimized
class Solution:

        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left,right) # or max(left,right) + 1

        