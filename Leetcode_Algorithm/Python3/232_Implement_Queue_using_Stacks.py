"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""

class Stack:
    def __init__(self):
        self.lst = []
        
    def __len__(self):
        return len(self.lst)
    
    def __str__(self):
        string = ""
        for x in self.lst:
            string += (str(x) + " ")
        return string
    
    def size(self):
        return len(self.lst)
    
    def empty(self):
        return len(self.lst) == 0
    
    def top(self):
        return self.lst[-1]
    
    def pop(self):
        if self.empty():
            print("stack is empty")
            return None
        return self.lst.pop()
    
    def push(self, obj):
        self.lst.append(obj)
        
    
class MyQueue:
    import copy
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = Stack()
        self.outStack = Stack()
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.push(x)
        print(self.inStack.empty())
        
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.inStack.empty():
            self.outStack.push(self.inStack.pop())
        output = self.outStack.pop()
        while not self.outStack.empty():
            self.inStack.push(self.outStack.pop())
        return output
            
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        temp = copy.deepcopy(self.inStack)
        output = 0
        while not temp.empty():
            output = temp.pop()
        return output
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.inStack.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()