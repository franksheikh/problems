# Time -> O(n)
# Space -> O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        ref = head

        while ref:
            save = ref.next
            ref.next = prev
            prev = ref
            ref = save
        return prev