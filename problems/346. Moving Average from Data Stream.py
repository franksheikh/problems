'''
Time - O(1)
Space - O(n)

'''
class MovingAverage:

    def __init__(self, size: int):
        self.max_size = size
        self.values = collections.deque()
        self.ps = 0

        

    def next(self, val: int) -> float:
        self.ps += val
        self.values.append(val)

        if self.values and len(self.values) > self.max_size:
            last_val = self.values.popleft()
            self.ps -= last_val
        
        return self.ps / len(self.values)





        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)