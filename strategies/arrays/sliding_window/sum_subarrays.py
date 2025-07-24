def find_length(nums, k):
	l = r = curr = ans = 0
	while r < len(nums):
		curr += nums[r]
		while curr > k:
			curr -= nums[l]
			l += 1
		ans = max(ans, r - l + 1)
		r += 1
	return ans

print(find_length([1,2,3,4,5],9))

'''
for right in range(len(nums))
'''