'''

abbaca
   ^

l = [
]


'''
# Time => O(n)
# Space => O(2n), n for populating stack, and n for creating an sized string from stack => O(n) final
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        
        return "".join(stack)

        