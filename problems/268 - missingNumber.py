class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        gs = n * (n + 1) // 2
        return gs - sum(nums)