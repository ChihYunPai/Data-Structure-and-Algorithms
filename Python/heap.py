"""
Implementation of heap
"""


import sys
import gc

class Heap:

	def __init__(self, array=[], opt='min'):

		if not (opt == 'min' or opt == 'max'): 
			raise ValueError("opt must be 'min'/'max'. ")
		else: 
			self.opt = opt

		self.array = []
		self.length = len(self.array)
		self.INT_MAXSIZE = -sys.maxsize if (opt == 'min') else sys.maxsize

		if array != []: 
			self.heapify(array)

	def __repr__(self):
		return str(self.array)

	def __str__(self):
		return str(self.array)

	def __len__(self):
		return self.length

	def __del__(self):
		del self.array
		del self.length
		del self
		gc.collect()

	def __cmp(self, a, b):
		return a < b if self.opt == 'min' else a > b

	def __parent(self, index):
		return (index-1)//2

	def __left(self, index):
		return (2*index + 1)

	def __right(self, index):
		return (2*index + 2)

	def __check(self, index=None):
		assert(0 <= index < self.length)
		if index == 0: return
		parent = self.__parent(index)
		if self.__cmp(self.array[index], self.array[parent]):
			self.array[index], self.array[parent] = self.array[parent], self.array[index]
			self.__check(parent)

	def __heapify(self, index):
		left = self.__left(index)
		right = self.__right(index)
		optimal = index
		if left < self.length and self.__cmp(self.array[left], self.array[optimal]):
			optimal = left
		if right < self.length and self.__cmp(self.array[right], self.array[optimal]):
			optimal = right
		if optimal != index:
			self.array[index], self.array[optimal] = self.array[optimal], self.array[index]
			self.__heapify(optimal)

	def heapify(self, lst):
		for item in lst:
			self.insert(item)

	def size(self):
		return self.length

	def empty(self):
		return self.length == 0

	def find(self, item=None):
		"""
		return index of the item starting search from root
		return None if the item is not in the heap
		"""
		for (index, x) in enumerate(self.array):
			if item == x:
				return index
		return None

	def top(self):
		return self.array[0] if self.length != 0 else None

	def pop(self):
		if self.length == 0: return None
		elif self.length == 1:
			self.length -= 1
			return self.array.pop(0)
		else:
			root = self.array.pop(0)
			self.length -= 1
			self.__heapify(0)
			return root

	def insert(self, item=None):
		self.array.append(item)
		self.length += 1
		self.__check(self.length - 1)

	def replace(self, item):
		"""
		pop root and push a new key. 
		"""
		assert(self.length > 0)
		self.array[0] = item
		self.__heapify(0)

	def delete(self, i):
		assert(0 <= i < self.length)
		self.array[i] = self.INT_MAXSIZE
		self.__check(i)
		self.pop()