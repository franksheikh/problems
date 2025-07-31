# Time -> O(n)
# Space -> O(1)

# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            left = str.lower(s[l])
            right = str.lower(s[r])
            if not str.isalnum(left):
                l += 1
                continue
            elif not str.isalnum(right):
                r -= 1
                continue
            elif left == right:
                l += 1
                r -= 1
            else:
                return False
        return True

# Solution 2
# Time -> O(n)
# Space -> O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
