# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(node):
            if not node:
                return
            if not node.left and val < node.val:
                node.left = TreeNode(val)
            if not node.right and val > node.val:
                node.right = TreeNode(val)
            
            if val > node.val:
                dfs(node.right)
            else:
                dfs(node.left)
        dfs(root)
        return root