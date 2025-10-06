'''

Time - O(n)
Space - O(n)

'''

from collections import deque

class RecentCounter:

    def __init__(self):
        self.deque = deque()
        

    '''
    3001
    lb = 2
    rb = 3002

    dq = [1, 100]

    '''
    def ping(self, t: int) -> int:
        left_bound = t - 3000
        right_bound = t

        while self.deque and self.deque[0] < left_bound:
            self.deque.popleft()
        self.deque.append(t)
        
        return len(self.deque)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)