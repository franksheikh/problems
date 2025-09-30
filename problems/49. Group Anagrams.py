'''
Given n n as the length of strs and m m as the average length of the strings, we iterate over each string and sort it, which costs O(n⋅m⋅logm). Then, we need to iterate over the keys. 

In the worst case scenario, when there are no matching anagrams, there will be n n groups, which means this will cost O ( n ) O(n), giving an overall time complexity of O(n⋅m⋅logm) (the final + n +n is dominated). 

The space complexity is O ( n ⋅ m ) O(n⋅m) as each string will be placed in an array within the hash map.

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            strings[sorted_key].append(s)
        return list(strings.values())