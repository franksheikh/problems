# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(node, curr_sum):
            if not node:
                return False
            if not node.left and not node.right:
                return curr_sum + node.val == targetSum
            
            curr_sum += node.val
            left = traverse(node.left, curr_sum)
            right = traverse(node.right, curr_sum)
            return left or right
        
        return traverse(root, 0)
        

# 2 Official
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def traverse(node, local_max):
            if not node:
                return 0
            
            new_max = max(local_max, node.val)
            left = traverse(node.left, new_max)
            right = traverse(node.right, new_max)

            ans = left + right
            if node.val >= local_max:
                ans += 1
            return ans

        
        return traverse(root, -inf)


