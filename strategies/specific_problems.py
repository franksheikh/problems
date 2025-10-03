'''

Find the number of subarrays with **exactly k** odd numbers in them.
- Giveaway for prefix sum with hashmap

"Number of subarrays" → counting subarrays (not finding one specific subarray)
"Exactly k [something]" → looking for curr - k in our prefix map
Contiguous subarray → prefix sum technique applies
'''


'''
Using ordinals to track character counters
'''
groups = {}

count = [0] * 26
for c in 'abc':
	count[ord(c) - ord('a')]+=1

key = tuple(count)
if key not in groups:
    groups[key] = []

print('groups',groups)