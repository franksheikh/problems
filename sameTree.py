# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' 
1. find Node
2. if not found, return false
3. if found, check each node matches
4. if not match, return false

PROBLEM
- values can be repeated
'''

class Solution:   
    def checkMatch(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        if p.val != q.val:
            return False
        return self.checkMatch(p.left, q.left) and self.checkMatch(p.right, q.right)
        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        
        if not subRoot:
            return False


        def findNode(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root or not subRoot:
                return
            
            if root.val == subRoot.val and self.checkMatch(root, subRoot):
                self.found = True
                

            findNode(root.left, subRoot)
            findNode(root.right, subRoot)
        
        findNode(root, subRoot)

        return self.found
        