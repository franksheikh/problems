class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
            
        count = 0
        l = 0
        curr = 1
        
        for r in range(len(nums)):
            curr *= nums[r]
            
            while curr >= k:
                curr //= nums[l]
                l += 1
            
            count += (r - l + 1)
        
        return count
    

# Official
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
                
            ans += right - left + 1

        return ans