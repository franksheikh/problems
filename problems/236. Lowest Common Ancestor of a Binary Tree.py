# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time - O(n) - might have to go down the entire left and right side, or is just straight line
# Space - O(n) - worst-case n recursive calls added to the call stack

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print('1')
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return None
        if left and right:
            return root
        if not left and right:
            return right
        if not right and left:
            return left
        
        # return right if right else left -> if left exists, it will be left, or else it will be right. but right may either exist or not, so that clause will capture the accurate result regardless