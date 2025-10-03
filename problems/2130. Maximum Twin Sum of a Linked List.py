# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        node = slow.next

        while node:
            save = node.next
            node.next = prev
            prev = node
            node = save
        
        slow.next = prev
        
        fast = slow.next
        slow = head

        max_ans = 0

        while fast:
            max_ans = max(max_ans, slow.val + fast.val)
            slow = slow.next
            fast = fast.next
        
        return max_ans

        

        
        

        