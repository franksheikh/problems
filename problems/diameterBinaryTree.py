# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0
    def maxDepth(self, root: Optional[TreeNode]):
        
        if not root:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        curr_depth = left_height + right_height

        self.max_depth = max(self.max_depth, curr_depth)

        return max(left_height, right_height) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)

        return self.max_depth
        