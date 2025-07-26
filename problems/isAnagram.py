from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = Counter(s)
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]
        return len(hashmap) == 0
