"""
Implementation of heap
"""
"""
build: O(n)
insert: O(log n)
update
top: O(1)
delete: O(log n)
heapify
"""


class heap(object):
	import sys
	INT_MIN = -sys.maxsize
	INT_MAX = sys.maxsize

	def __init__(self, lst=[], opt='min'):
		assert(opt=='min' or opt=='max')
		self.heap = []
		self.opt = opt
		# if len(self.heap) > 0:
		# 	self.__heapify(0)
		for x in lst:
			self.insert(x)

	def __len__(self):
		return len(self.heap)

	def __str__(self):
		string = ""
		for x in self.heap:
			string += (str(x) + " ")
		return string

	def __cmp(self, a, b):
		return a > b if self.opt=='min' else a < b

	def __swap(self, a, b):
		a, b = b, a

	def __parent(self, i):
		return i//2
		# if not (0 <= index <= len(self.heap)): return None
		# return self.heap[index]

	def __left(self, i):
		return (2*i) + 1
		# if not (0 <= index <= len(self.heap)): return None
		# return self.heap[index]

	def __right(self, i):
		return (2*i) + 2
		# if not (0 <= index <= len(self.heap)): return None
		# return self.heap[index]

	def __check(self, i):
		while i > 0 and self.__cmp(self.heap[self.__parent(i)], self.heap[i]):
			self.__swap(self.heap[i], self.heap[self.__parent(i)])
			i = self.__parent(i)

	def __decreaseKey(self, i, x):
		self.heap[i] = x
		self.__check(i)

	def __heapify(self, i):
		left = self.__left(i)
		right = self.__right(i)

		optimal = i
		print(left, right, optimal)
		if left < len(self.heap) and self.__cmp(self.heap[i], self.heap[left]):
			optimal = left
		if right < len(self.heap) and self.__cmp(self.heap[optimal], self.heap[right]):
			optimal = right
		if optimal != i:
			self.__swap(self.heap[i], self.heap[optimal])
			self.__heapify(optimal)

	def size(self):
		return len(self.heap)

	def empty(self):
		return self.size == 0

	def top(self): # aka. peek
		return None if self.empty() else self.heap[0]

	def pop(self): # aka. extract min/max
		if len(self.heap) <= 0:
			return None
		elif len(self.heap) == 1:
			return self.heap.pop()
		root = self.heap[0]
		self.heap[0] = self.heap.pop()
		self.__heapify(0)
		return root

	def insert(self, x):
		self.heap.append(x)
		self.__check(len(self.heap) - 1)

	def delete(self):
		self.__decreaseKey(i, INT_MIN)
		self.pop()

	def replace(self, x):
		"""
		pop root and push a new key.
		"""
		root = self.pop()
		if len(self.heap) <= 0:
			return None
		elif len(self.heap) == 1:
			root = self.heap[0]
			self.heap[0] = x
			return root

		root = self.heap[0]
		self.heap[0] = x
		self.__heapify(0)
		return root

	# def merge(self):

	# def meld(self):


#### test ####
lst=[5,4,3,2,1]
heap = heap(lst)
print(heap)

