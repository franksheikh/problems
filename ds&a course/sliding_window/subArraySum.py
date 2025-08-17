'''
To summarize:

- We use curr to track the prefix sum.
- At any index i, the sum up to i is curr. If there is an index j whose prefix is curr - k, then the sum of the subarray with elements from j + 1 to i is curr - (curr - k) = k.
- Because the array can have negative numbers, the same prefix can occur multiple times. We use a hash map counts to track how many times a prefix has occurred.
- At every index i, the frequency of curr - k is equal to the number of subarrays whose sum is equal to k that end at i. Add it to the answer.

The time and space complexity of this algorithm are both O ( n ) O(n), where n n is the length of nums. Each for loop iteration runs in constant time and the hash map can grow to a size of n n elements.
'''

# Time and Space => O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int,{0:1})
        curr = 0
        c = 0
        for n in nums:
            curr += n
            c += counts[curr - k]
            counts[curr] = counts.get(curr,0) + 1
        return c
        