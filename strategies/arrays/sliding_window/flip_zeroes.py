'''
NEW
'''
def find_length1(s):
	left = curr = ans = 0
	for right in range(len(s)):
		if s[right] == '0':
			curr += 1
		while curr > 1:
			if s[left] == '0':
				curr -= 1
			left += 1
				
		ans = max(ans, right - left + 1)
	return ans



'''
OLD
'''
def find_length2(nums):
	left = curr = ans = 0
	f = False

	for right in range(len(nums)):
		v = nums[right]
		if v == '0' and f:
			left = right - 1
			f = False
		if v == '0' and not f:
			f = True
		
		ans = max(ans, right - left + 1)
	
	return ans


		
print('first:',find_length1('011010111'))
print('second:',find_length2('011010111'))