# [1,3,6,10,15]
# #  i 
# #    j

# i = 1
# j = 3
# nums[j] - nums[i-1]

def answer_queries(nums, queries, limit):
	prefix=[nums[0]]
	res = []
	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[len(prefix) - 1])
	for i, j in queries:
		if i == 0:
			res.append(prefix[j] < limit)
		else:
			res.append((prefix[j] - prefix[i-1]) < limit)
	return res

print(answer_queries([1,2,3,4,5],[[0,4]],16))

""" OR """


def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans