from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        r_count = Counter(ransomNote)
        for char in magazine:
            if char in r_count:
                r_count[char] -= 1
                if r_count[char] == 0:
                    del r_count[char]
        return len(r_count.keys()) == 0
        