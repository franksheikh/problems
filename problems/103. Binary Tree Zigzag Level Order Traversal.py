# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        stack = []
        is_left = True

        while q:
            n = len(q)
            local_q = collections.deque()

            for _ in range(n):
                node = q.popleft()

                if is_left:
                    local_q.append(node.val)
                else:
                    local_q.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            stack.append(list(local_q))
                
            is_left = not is_left
        
        return stack

        
        