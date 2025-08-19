class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            strings[sorted_key].append(s)
        return list(strings.values())