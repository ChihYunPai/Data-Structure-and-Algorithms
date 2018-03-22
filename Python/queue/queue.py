from array import  array

class Queue(array):
	# Queue

	def __init__(self, size=0, value=0):
		self.body = array(size, value)

	def __str__(self):
		return self.body.__str__()

	def empty(self):
		return self.body.empty()

	def size(self):
		return self.body.size()

	def front(self):
		return self.body.front()

	def back(self):
		return self.body.back()

	def push(self, object):
		self.body.push_back(object)

	def pop(self):
		return self.body.pop_front()

	def swap(self, other_queue):
		self.body, other_queue.body = other_queue.body, self.body