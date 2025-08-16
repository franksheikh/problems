# SLIDING WINDOW
# Time complexity -> O(n) -> Amortized
# Space complexity -> O(1)
def longest_sub_less_than_or_equal_to_k(nums,k):
    i = 0
    j = 0
    max_l = 0
    curr = 0
    l = len(nums)
    
    while j < l:
        curr += nums[j]
        while curr > k:
            curr -= nums[i]
            i += 1
        
        max_l = max(max_l, j - i + 1)
        j += 1
    
    return max_l
            
        
nums = [5,4,3,2,1,1,1,1]

print(longest_sub_less_than_k(nums,5))
print('here')

# official solution
def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans