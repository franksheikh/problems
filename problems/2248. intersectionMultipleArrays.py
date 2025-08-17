'''
Let's say that there are n lists and each list has an average of m elements. To populate our hash map, it costs O(n · m) to iterate over all the elements. The next loop iterates over all unique elements that we encountered. If all elements are unique, this can cost up to O(n · m), although this won't affect our time complexity since the previous loop also cost O(n · m). Finally, there can be at most m elements inside ans when we perform the sort, which means in the worst case, the sort will cost O(m · log m). This gives us a time complexity of O(n · m + m · log m) = O(m · (n + log m)). If every element in the input is unique, then the hash map will grow to a size of n · m, which means the algorithm has a space complexity of O(n · m)
'''

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for arr in nums[1:]:
            res &= set(arr)
        return sorted(res)