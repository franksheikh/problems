# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        

# iterative
class Solution2:
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False
        stack = [p,q]
        while stack:
            p_node = stack.pop()
            q_node = stack.pop()

            if not p_node and not q_node:
                continue
            elif p_node and not q_node or q_node and not p_node:
                return False
            elif p_node and q_node and p_node.val != q_node.val:
                return False
            else:
                stack.append(p_node.left)
                stack.append(q_node.left)
                stack.append(p_node.right)
                stack.append(q_node.right)
        
        return True