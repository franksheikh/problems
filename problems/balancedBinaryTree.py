# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self, node):
        if not node:
            return 0
        
        left = self.checkHeight(node.left)
        if left == -1:
            return -1
        right = self.checkHeight(node.right)
        if right == -1:
            return -1
        

        
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkHeight(root) != -1
        
        

'''
[
    (2,1),
    (4,2),
    (5,2)
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.height_balanced = True

    def getHeight(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left_height = 1 + self.getHeight(root.left)
        right_height = 1 + self.getHeight(root.right)

        if abs(left_height -  right_height) > 1:
            self.height_balanced = False
        
        return max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.getHeight(root)
        res = self.height_balanced
        self.height_balanced = True
        return res