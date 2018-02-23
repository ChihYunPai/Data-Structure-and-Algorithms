"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        
    def __len__(self):
        return len(self.lst)
    
    def empty(self):
        return len(self.lst) == 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.lst.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            print("stack is empty.")
            return None
        return self.lst.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            print("stack is empty.")
            return None
        return self.lst[-1]
        
    def peekMax(self):
        """
        :rtype: int
        """
        if self.empty():
            print("stack is empty.")
            return None
        return max(self.lst)
    
    def popMax(self):
        """
        :rtype: int
        """
        if self.empty():
            print("stack is empty.")
            return None
        return self.lst.pop(len(self.lst) - self.lst[::-1].index(max(self.lst)) - 1)

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()