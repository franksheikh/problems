# Time complexity: O(m * n)
# Space complexity: O(m + n)
class Solution:   
    def checkMatch(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif not q and p or not p and q:
            return False
        elif p.val != q.val:
            return False
        return self.checkMatch(p.left, q.left) and self.checkMatch(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.checkMatch(root, subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)