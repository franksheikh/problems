from collections import Counter

# Time complexity: O(n)
# Space complexity: O(1) - only 26 characters
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1