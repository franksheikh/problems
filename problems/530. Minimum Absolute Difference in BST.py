# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        seen = []
        min_diff = inf

        def dfs(node):
            nonlocal min_diff
            if not node:
                return
            dfs(node.left)
        
            if seen:
                min_diff = min(min_diff, abs(node.val - seen[-1]))
                seen.pop()
            seen.append(node.val)
            dfs(node.right)
        dfs(root)
        return min_diff



        