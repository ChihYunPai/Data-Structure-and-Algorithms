"""
Data Structures useful for implementing searching
"""
import queue

class Stack:
	def __init__(self):
		self.stack = queue.LifoQueue()

	def __len__(self):
		return self.stack.qsize()

	def size(self):
		return self.stack.size()

	def push(self, item):
		self.stack.put(item)

	def pop(self):
		return self.stack.get()

	def empty(self):
		return self.stack.empty()

class Queue():
	def __init__(self):
		self.queue = queue.Queue()

	def __len__(self):
		return self.queue.qsize()

	def size(self):
		return self.queue.size()

	def push(self, item):
		self.queue.put(item)

	def pop(self):
		return self.queue.get()

	def empty(self):
		return self.queue.empty()

class PQueue():
	def __init__(self, priorityFunction=None):
		self.pqueue = queue.PriorityQueue()
		self.priorityFunction = priorityFunction

	def __len__(self):
		return self.pqueu.qsize()

	def _getPriority(self, item):
		try:
			return self.priorityFunction(item)
		except:
			raise ValueError("self.priorityFunction(item) is not a valid function.")

	def size(self):
		return self.pqueue.size()

	def push(self, item, priority=None):
		if priority:
			self.pqueue.put((priority, item))
		else:
			self.pqueue.put((self._getPriority(item)))

	def pop(self):
		(priority, item) = pqueue.get()
		return item

	def pop_prority_item(self):
		return pqueue.get()

class PQueueWithFunction(PQueue):
    def  __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        PQueue.__init__(self)

    def push(self, item):
        PriorityQueue.push(item, self.priorityFunction(item))


def manhattanDistance(xy1, xy2):
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def euclideanDistance(xy1, xy2):
    return ((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)**.5

def chebyshevDistance(xy1, xy2):
	return max(abs(xy[0] - xy2[0]), abs(xy[1] - xy[1]))