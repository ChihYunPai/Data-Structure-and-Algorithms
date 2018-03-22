from array import Array

class Stack(array):
	# Stack

	def __init__(self, size=0, value=0):
		self.body = Array(size, value)

	def __str__(self):
		return self.body.__str__()

	def empty(self):
		return self.body.empty()

	def size(self):
		return self.body.size()

	def top(self):
		return self.body.back()

	def push(self, object):
		self.body.push_back(object)

	def pop(self):
		return self.body.pop_back()

	def swap(self, other_stack):
		self.body, other_stack.body = other_stack.body, self.body
