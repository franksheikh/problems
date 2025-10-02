# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        prev = dummy
        ref = head

        while ref and ref.next:
            first = ref
            second = ref.next

            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
            ref = first.next
        
        return dummy.next