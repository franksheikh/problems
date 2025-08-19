class Solution:
    def sumDigits(self,n):
        digit_sum = 0
        while n:
            digit_sum += n % 10
            n = n // 10
        return digit_sum
    
    def maximumSum(self, nums: List[int]) -> int:
        o = defaultdict(lambda: [-1,-1])
        max_v = -1
        for n in nums:
            digit_sum = self.sumDigits(n)
            largest, second = o[digit_sum]
        
            if n > largest:
                second = largest
                largest = n
            elif n > second:
                second = n
            
            
            o[digit_sum] = [largest,second]
            if largest > -1 and second > -1:
                max_v = max(max_v, largest + second)
        
        return max_v
            
