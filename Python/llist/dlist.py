"""
Implementation of Double-Linked List
"""
import sys
import gc
class Node(object):
	def __init__(self, data=None, previous=None, next=None):
		self.data = data
		self.previous = previous
		self.next = next

	def __del__(self):
		del self
		gc.collect()

class DList(object):
	def __init__(self, head=None):
		self.head = head
		self.tail = None
		self.length = int(0)
		
		if head != None:
			previous = None
			current = self.head
			while current:
				self.length += 1
				previous = current
				current = current.next
			self.tail = previous

	def __str__(self):
		if self.head == None: return 'None'
		string = ''
		current = self.head
		while current:
			string += str(current.data) + ' '
			current = current.next
		return string

	def __len__(self):
		return self.length

	def __del__(self):
		current = self.head
		while current:
			previous = current
			current = current.next
			del previous
		del self
		gc.collect()

	def length(self):
		return self.length

	def display(self, opt='forward'):
		"""
		display(opt='forward'): forward display the compelete list
		display(opt='backward'): backward display the compelete list
		"""
		if opt == 'forward':
			print(self)
		elif opt == 'backward':
			previous = None 
			current = self.tail
			while current:
				print(current.data, end=' ')
				previous = current
				current = current.previous
		else: 
			raise ValueError('opt=\'forward\' / \'backward\'')

	def delete(self):
		"""
		delete the whole list
		"""
		current = self.head
		while current:
			previous = current
			current = current.next
			del previous
		self.head = self.tail = None 
		self.length = int(0)
			
	def empty(self):
		"""
		return is list empty
		"""
		return self.head == None

	def add(self, item):
		self.insert_front(item)

	def insert_front(self, item):
		"""
		insert item before the head
		"""
		node = Node(item)
		# case1: length = 0:
		if self.length == 0:
			self.head = self.tail = node
		# case2: length >= 1:
		else:
			self.head.previous = node
			node.next = self.head
			self.head = node
		self.length += 1

	def insert_back(self, item):
		"""
		inser item after the tail
		"""
		node = Node(item)
		# case1: length = 0:
		if self.length == 0:
			self.head = self.tail = node
		# case2: length >= 1:
		else:
			self.tail.next = node
			node.previous = self.tail
			self.tail = node
		self.length += 1

	def insert(self, item=None, key=None, opt='forward'):
		"""
		insert item before key if found forwardly (opt='forward') or backwardly (opt='backward'), opt default 'forward'
		if the key is not given(key==None), 
			opt='forward' is equivalent to insert_front(item)
			opt='backward' is equivalent to insert_back(item)
		if the key is given,
			opt='forward' search the key from head
			opt='backward' search the key from tail
		return True if found the key and successfully inserted the item
		"""
		assert(item!=None)
		if opt == 'forward': current = self.head
		elif opt == 'backward': current = self.tail
		else: raise ValueError('opt should be eighter \'forward\' or \'backward\'. ')
		while current:
			if current.data == key:
				if current == self.head and opt=='forward': 
					self.insert_front(item)
					return True
				elif current == self.tail and opt=='backward': 
					self.insert_back(item)
					return True
				else:
					node = Node(item)
					if opt=='forward':
						current.previous.next = node
						node.previous = current.previous
						current.previous = node
						node.next = current

					elif opt=='backward':
						current.next.previous = node
						node.next = current.next
						current.next = node
						node.previous = current

					else: pass

				self.length += 1
				return True
			if opt=='forward': current = current.next
			else: current = current.previous
		return False

	def search(self, item):
		"""
		return True if found item, else return False
		"""
		current = self.head
		while current:
			if current.data == item: return True
			current = current.next
		return False

	def remove(self, item=None, opt='forward'):
		"""
		remove item, return True if found and seccessfully removed, else return False if not found.
		"""
		assert(item!=None)
		if opt == 'forward': current = self.head
		elif opt == 'backward': current = self.tail
		else: raise ValueError('opt should be eighter \'forward\' or \'backward\'. ')
		while current:
			if current.data == item:
				if self.length == 1:
					self.head = self.tail = None
				else: # self.length > 1
					if current == self.head: 
						current.next.previous = None
						self.head = current.next
					elif current == self.tail:
						current.previous.next = None
						self.tail = current.previous
					else: # current in the middle
						current.next.previous = current.previous
						current.previous.next = current.next
				del current
				self.length -= 1
				return True
			if opt == 'forward': current = current.next
			else: current = current.previous
		return False

	def reverse(self):
		"""
		reverse all linked list
		"""
		if self.length <= 1: return False
		current = self.head
		while current:
			temp = current.previous
			current.previous = current.next
			current.next = temp
			current = current.previous
		self.head, self.tail = self.tail, self.head
