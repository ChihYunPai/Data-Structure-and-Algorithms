"""
Implementation of Double-Linked List
"""

class Node(object):
	def __init__(self, data=None, previous=None, next=None):
		self.data = data
		self.previous = previous
		self.next = next

class DList(object):
	def __int__(self, head=None):
		self.head = head
		if head != None:
			self.size = head.size
		else:
			self.size = 0

	def __str__(self):
		if self.head == None: return 'None'
		string = ''
		current = self.head
		while current:
			string += str(current.data) + ' '
			current = current.next
		return string

	def __len__(self):
		return self.size

	def display(self):
		"""
		display: displays the compelete list
		"""
		print(self)

	def delete(self):
		"""
		delete the whole list
		"""
		self.head = None

	def empty(self):
		"""
		return is list empty
		"""
		return self.head == None

	def add(self, item):
		"""
		add an element at the beginning of the list
		"""
		node = Node(item)
		node.next = self.head
		self.head = node
		self.size += 1

	def search(self, item):
		"""
		return True if found item, else return False
		"""
		current = self.head
		while current:
			if current.data == item: return True
			current = current.next
		return False

	def remove(self, item):
		"""
		remove item, return True if has removed the item, else return False if not found
		"""
		previous = None
		current = self.head
		found = False
		while current and found is False:
			if current.data == item:
				found = True
			else:
				previous = current
				current = current.next
		if found:
			if previous == None:
				self.head = current.next
			else:
				previous.next = current.next
			self.size -= 1
			return True
		else:
			return False

	def reverse(self):
		"""
		reverse all linked list
		"""
		if self.size <= 1: return False
		previous = None
		current = self.head
		while current.next:
			nextNode = current.next
			current.next = previous
			previous = current
			current = nextNode
		self.head = current
		current.next = previous
		return True

