# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''

i = 0
set dummy node 
ref = dummy.next
iterate from i to left

j = left
iterate from j to right
reverse function

return dummy.next


-> X

save = node.next
X
node.next = prev
3 -> 2 -> 1 -> None
prev = node
3 - > 2 -> 1 -> None
node = save
3





'''
class Solution:
    def reverseList(self, node, swap_amount):
        reversed = None
        save = None
        i = 0

        while(node and i < swap_amount):
            save = node.next
            node.next = reversed
            reversed = node
            node = save
            i += 1
        
        return [reversed, node]



    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        ref = dummy
        prev = ref
        li = 0
        
        while li < left - 1:
            prev = prev.next
            li += 1
        
        # Prev = section right before reverse

        # Section we want to reverse  
        node = prev.next
        # Reversed Section
        reversed, endNode = self.reverseList(node, right-left + 1)

        prev.next.next = endNode
        prev.next = reversed
        
        return dummy.next