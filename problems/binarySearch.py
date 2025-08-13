# Time -> O(logn)
# Space -> O(1)



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)

        while s < e:
            m = (s + e) // 2
            mid = nums[m]

            if mid == target:
                return m
            elif mid < target:
                s = m + 1
            else:
                e = m
        return -1


# This approach is wrong -> O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            mV = nums[m]

            if mV == target:
                return m
            elif target > mV:
                l += 1
            else:
                r -= 1
        
        return -1
        