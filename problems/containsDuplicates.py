class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for item in nums:
            if item in hashset:
                return True
            else:
                hashset.add(item)
        return False
        