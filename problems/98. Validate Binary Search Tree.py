# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True
            
            if node.val <= small or node.val >= large:
                return False

            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)

            return left and right
            
        
        return dfs(root, -inf, inf)

        


        