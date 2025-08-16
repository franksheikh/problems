# Time complexity: O(n) to preprocess, O(n) to answer each quwry
def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    ans = []
    for x,y in queries:
        # Handling edge case for left boundary is 0
        curr = prefix[y] - prefix[x] = nums[x]
        ans.append(curr < limit)
    return ans