# Time O(n) // wrong -> O(logn)
# Space O(n)
class Solution:
    def cycle_track(self, nc:int):
        sd = 0

        while nc > 0:
            r = (nc % 10) ** 2
            sd += r
            nc = nc // 10
        
        return sd

    def isHappy(self, n: int) -> bool:
        seen = set()
        sd = self.cycle_track(n)
        
        if sd == 1:
            return True
        
        while sd not in seen:
            seen.add(sd)
            sd = self.cycle_track(sd)
            
            if sd == 1:
                return True

        return False
