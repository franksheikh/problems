def find_best_subarray_fixed(nums, k):
	curr = 0
	for i in range(k):
		curr += nums[i]
	ans = curr
	for i in range(k,len(nums)):
		curr += nums[i]
		curr -= nums[i - k]
		ans = max(curr, ans)
	return ans

print(find_best_subarray_fixed([1,2,3,4,5],2))