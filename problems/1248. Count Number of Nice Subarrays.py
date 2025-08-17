from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int,{0:1})
        curr = 0
        c = 0
        for n in nums:
            curr += n % 2
            c += counts[curr - k]
            counts[curr] = counts.get(curr,0) + 1
        return c
            

        