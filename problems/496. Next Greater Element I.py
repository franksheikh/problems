class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # edge cases

        # base
        ans = []

        map = defaultdict(int)
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                last = stack.pop()
                map[last] = n
            stack.append(n)
        
        return [map.get(n,-1) for n in nums1]

             

        