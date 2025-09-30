from collections import Counter

# Time complexity: O(n)
# Space complexity: O(1) - only 26 characters
# A more general answer would be to say that the space complexity is O(k), where k is the number of characters

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1