'''
Problem:
Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
'''

'''
make array from i to k

for i = k, iterate to len nums
	add nums[i]
	remove nums[i-k]
	sum is max of new_sum compared to old sum

return su,
'''

# Official
def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans

def find_best_subarray2(nums,k):
    l = []
    max_sum = 0
    for i in range(0, k):
        l.append(nums[i])
    
    max_sum = sum(l)
    curr = max_sum
    for j in range(k, len(nums)):
        l.append(nums[j])
        
        curr += nums[j]
        curr -= nums[j-k]
        max_sum=max(curr,max_sum)
    
    return max_sum



def find_best_subarray3(nums,k):
    l = []
    max_sum = 0
    for i in range(0, k):
        l.append(nums[i])
    
    max_sum = sum(l)
    
    for j in range(k, len(nums)):
        l.append(nums[j])
        print('k',k,'j',j)
        max_sum = max(max_sum, sum(l[j-k+1:j+1]))
    
    return max_sum

print('findBest', find_best_subarray([1,2,3,4,5],2))
        
    
        
    