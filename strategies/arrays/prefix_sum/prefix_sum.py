# A prefix sum represents the sum of all prefixes.
# it is a form of preprocessing.
	# Building a prefix sum is a form of pre-processing. Pre-processing is a useful strategy in a variety of problems where we store pre-computed data in a data structure before running the main logic of our algorithm. While it takes some time to pre-process, it's an investment that will save us a huge amount of time during the main parts of the algorithm.

def prefix_sum(nums):
	prefix=[nums[0]]
	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[i-1])
	return prefix

print(prefix_sum([1,2,3,4,5]))