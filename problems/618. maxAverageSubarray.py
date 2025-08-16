class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k < 1:
            return 0
        curr = 0
        for i in range(0,k):
            curr += nums[i]
        max_avg = avg = curr / k
        for i in range(k,len(nums)):
            curr += nums[i] - nums[i-k]
            avg = curr / k
            max_avg = max(max_avg, avg)
        
        return max_avg
        

        