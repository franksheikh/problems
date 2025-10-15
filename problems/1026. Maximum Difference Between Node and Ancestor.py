# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_nsf, min_nsf):
            if not node:
                return 0
            
            abs_diff = max(abs(max_nsf - node.val), abs(min_nsf - node.val))
            
            n_max = max(max_nsf, node.val)
            n_min = min(min_nsf, node.val)
            
            left = dfs(node.left, n_max, n_min)
            right = dfs(node.right, n_max, n_min)

            return max(abs_diff, left, right)
        

        return dfs(root, root.val, root.val)
        
        
        
        
