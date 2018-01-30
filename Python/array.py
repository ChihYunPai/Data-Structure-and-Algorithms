class array:
	# Array

	def __init__(self, size=0, value=0):
		self.list = [value]*size

	def __str__(self):
		string = str('')
		for item in self.list:
			string += (str(item) + ' ')
		return string

	def __len__(self):
		return len(self.list)

	def __getitem__(self, index):
		return self.list[index]

	def __setitem__(self, index, item):
		self.list[index] = item

	def __delitem__(self, index):
		del self.list[index]

	def __contains__(self, item):
		return item in self.list

	def __iter__(self):
		return iter(self.list)

	def __reversed__(self):
		return reversed(self.list)

	def remove(self, object):
		self.list.remove(object)

	def delete(self, index):
		del self.list[index]

	def size(self):
		return len(self.list)

	def at(self, index):
		return self.list[index]

	def front(self):
		return self.list[0]

	def back(self):
		return self.list[-1]

	def insert(self, index, item):
		self.list.insert(index, item)

	def push_front(self, item):
		self.list.insert(0, item)

	def push_back(self, item):
		self.list.append(item)

	def pop_front(self):
		return self.list.pop(0)

	def pop_back(self):
		return self.list.pop()

	def empty(self):
		return self.list==[]

	def swap(self, index1, index2):
		self.list[index1], self.list[index2] = self.list[index2], self.list[index1]