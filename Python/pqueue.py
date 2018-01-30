import heapq

class PQueue(array):
	# Implementation of Priority Queue using heapq

	def __init__(self):
		self.heap = []

	def __str__(self):
		return str(self.heap)

	def __len__(self):
		return len(self.heap)

	def empty(self):
		return self.heap==[]

	def size(self):
		return len(self.heap)
		
	def push(self, item, priority=0):
		heapq.heappush(self.heap, (priority, item))

	def pop(self):
		(priority, item) = heapq.heappop(self.heap)
		return item

	def pop_priority_item(self):
		return heapq.heappop(self.heap)

	def front(self):
		"""
		to see the top item(smallest priority) in the pqueue
		"""
		return heapq.nsmallest(1, self.heap)

	def back(self):
		"""
		to see the back item(largest priority) in the pqueue
		"""
		return heapq.nlargest(1, self.heap)

	def isIn(self, item):
		for x in self.heap:
			if x[1] == item: return True
		return False

	def getPriority(self, item):
		for x in self.heap:
			if x[1] == item: return x[0]
		return False