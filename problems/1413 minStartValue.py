class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        rs = 0
        min_value = None
        for i in range(len(nums)):
            rs += nums[i]
            
            if not min_value:
                min_value = rs
            else:
                min_value = min(min_value, rs)   
            
        return 1 if min_value >= 0 else abs(min_value) + 1
                
            
        
        