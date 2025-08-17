'''
b:1
a:1
l:2
o:2
n:1

'''
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = Counter(text)
        chars['l'] //= 2
        chars['o'] //= 2

        return min(
            chars['b'],
            chars['a'],
            chars['l'],
            chars['o'],
            chars['n'],
        )
