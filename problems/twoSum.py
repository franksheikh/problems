# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                # min_v = min(hashmap[diff], idx)
                # max_v = max(hashmap[diff], idx)
                return [hashmap[diff], idx]
            else:
                hashmap[val]  = idx
        
        

        