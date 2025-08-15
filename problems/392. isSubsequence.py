# Time O(n)
# Space O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = 0
        lt = 0
        t_len = len(t)
        s_len = len(s)

        if s_len > t_len:
            return False

        while lt < t_len:
            if ls == s_len:
                return True
            if s[ls] == t[lt]:
                ls += 1
            lt += 1
        
        return ls == s_len
