class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l = [-1] * len(nums)
        d = k * 2 + 1
        if k < 1:
            return nums
        if d > len(nums):
            return l

        ps = 0

        for i in range(d):
            ps += nums[i]
        
        l[k] = ps // d
        
        for i in range(k+1, len(nums) - k):
            ps += nums[i + k] - nums[i - k - 1]
            l[i] = ps // d
        
        return l




        