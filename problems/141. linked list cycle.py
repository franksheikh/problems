# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''

1 -> 3 -> 5 -> 7
     ^         |
     |         |
	 |_________|

s
    f
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if fast == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next
        return False
            