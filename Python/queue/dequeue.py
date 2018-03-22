from array import array

class dequeue(array):
	# double-ended queue

	def __init__(self, size=0, value=0):
		self.body = array(size, value)

	def __str__(self):
		return self.body.__str__()

	def empty(self):
		return self.body.empty()

	def size(self):
		return self.body.size()

	def at(self, index):
		return self.body.at(index)

	def front(self):
		return self.body.front()

	def back(self):
		return self.body.back()

	def push_front(self, object):
		self.body.push_front(object)

	def push_back(self, object):
		self.body.push_back(object)

	def pop_front(self):
		return self.body.pop_front()

	def pop_back(self):
		return self.body.pop_back()

	def swap(self, other_dequeue):
		self.body, other_dequeue.body = other_dequeue.body, self.body