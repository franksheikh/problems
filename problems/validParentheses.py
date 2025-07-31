# Solution 1
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
            if char in chars:
                l.append(char)
            else:
                if not l or chars[l.pop()] != char:
                    return False

            
            
        return len(l) == 0