
# Solution 1
# Push only opening brackets, or unclosed brackets
class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        ans = []
        for char in s:
            if char in chars:
                if not ans or ans.pop() != chars[char]:
                    return False
            else:
                ans.append(char)
        return not ans

# Solution 2
# Time -> O(n)
# Space -> O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '{':'}',
            '(':')',
            '[':']'
        }

        l = []

        for char in s:
            
            if len(l) and l[-1] in chars and chars[l[-1]] == char:
                l.pop()
            else:
                l.append(char)
            
        return len(l) == 0

# Solution 3
# Time -> O(n)
# Space -> O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '{':'}',
            '(':')',
            '[':']'
        }

        l = []

        for char in s:
            if char in chars:
                l.append(char)
            else:
                if not l or chars[l.pop()] != char:
                    return False

            
            
        return len(l) == 0
    

# Version 3
class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '[':']',
            '{':'}',
            '(':')'
        }

        stack = []

        for c in s:
            if c in chars:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif chars[stack.pop()] != c:
                    return False
        return len(stack) == 0