# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''

'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        curr = 0 if (root.val < low or root.val > high) else root.val
        
        return curr + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
time and space are O(n) because you could have a straight line, with the root node the max and every value to the left being greater than the low
'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # only left side, since current node and right too high
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # only right side, since current node and left too low
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        