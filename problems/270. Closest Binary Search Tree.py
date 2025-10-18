# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
 Every value distinct?
'''
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_value = inf
        min_diff = inf
        def dfs(node):
            nonlocal min_value
            nonlocal min_diff

            if not node:
                return
            
            if target - node.val == 0:
                min_value = node.val
                min_diff = 0
            
            curr_diff = abs(target - node.val)
            
            if curr_diff == min_diff:
                min_value = min(node.val, min_value)

            elif curr_diff < min_diff:
                min_value = node.val
                min_diff = curr_diff
            
            if target < node.val:
                dfs(node.left)
            
            elif target > node.val:
                dfs(node.right)
        dfs(root)
        return min_value

