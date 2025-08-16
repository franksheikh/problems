'''
[1,1,0,0,0,1,1]
       l
             r

k = 2
curr_k = 2

'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        curr_k = 0
        l = 0
        
        for r in range(0, len(nums)):
            if nums[r] == 0:
                curr_k += 1
            while curr_k > k:
                if nums[l] == 0:
                    curr_k -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans