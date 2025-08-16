
# Prefix Sum way
# Time O(n)
# Space O(n)
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        rs = 0
        ts = sum(nums)
        c = 0
        for i in range(len(nums)-1):
            rs += nums[i]
            if rs >= ts - rs:
                c += 1
        return c
                
            
        
    def waysToSplitArray2(self, nums: List[int]) -> int:
        ways = 0
        j = len(nums) - 1
        ps = [nums[0]]
        for i in range(1,len(nums)):
            ps.append(nums[i] + ps[-1])
        for i in range(1, len(nums)):
            left_half = ps[i-1]
            right_half = ps[j] - ps[i-1]
            if left_half >= right_half:
                ways += 1
        return ways
        