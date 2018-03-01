"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

from collections import deque
class MovingAverage:
    """
    First version
    """
#     def __init__(self, size):
#         """
#         Initialize your data structure here.
#         :type size: int
#         """
#         self.size = size
#         self.lst = []
        
        

#     def next(self, val):
#         """
#         :type val: int
#         :rtype: float
#         """
        
#         self.lst.append(val)
#         if len(self.lst) < self.size:
#             return sum(self.lst) / len(self.lst)
#         else:
#             return sum(self.lst[len(self.lst) - self.size:]) / self.size
        
    """
    Second version
    """
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0
        self.queue = deque()
        self.size = size
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) < self.size:
            self.sum += val
            self.queue.append(val)
        else:
            self.sum += (val - self.queue.popleft())
            self.queue.append(val)
        return self.sum / len(self.queue)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)