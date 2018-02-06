import sys
import gc

class Node:
	def __init__(self, item=None, left=None, right=None):
		self.item = item
		self.left = left
		self.right = right

	def __repr__(self):
		return repr(self.item) + ' ' + repr(self.left) + ' ' + repr(self.right)

	def __str__(self):
		return str(self.item) + ' ' + str(self.left) + ' ' + str(self.right)

	def __del__(self):
		del self
		gc.collect()

class BTree:
	def __init__(self, root=None):
		self.root = root

	def __repr__(self):
		return repr(self.root)

	def __str__(self):
		return str(self.root)

	def __del__(self):
		del self.root
		gc.collect()

	def __len__(self):
		return len([x for x in list(str(self.root).split(' ')) if x != 'None'])

	def __iter__(self):
		if self.root != None:
			return iter(self.root)
		else:
			return iter([])

	def insert(self, item=None):
		"""
		insert implemented in iteration method
		"""
		if self.root == None:
			self.root = Node(item)
		else:
			# parent = None
			current = self.root
			while(True):
				if item < current.item:
					if current.left == None:
						current.left = Node(item)
						break
					current = current.left
				else:
					if current.right == None:
						current.right = Node(item)
						break
					current = current.right

	# def insert(self, item=None):
	# 	"""
	# 	insert implemented in recursive method
	# 	"""
	# 	if self.root == None:
	# 		self.root = Node(item)
	# 	else:
	# 		self.__insert(item, self.root)

	# def __insert(self, item=None, node=None):
	# 	"""
	# 	subfunction __insert implemented in recursive method
	# 	"""
	# 	if node == None:
	# 		return Node(item)
	# 	else:
	# 		if item < node.item:
	# 			if node.left == None:
	# 				print('left: ', node.item)
	# 				node.left = Node(item)
	# 			else:
	# 				self.__insert(item, node.left)
	# 		else:
	# 			if node.right == None:
	# 				print('right: ', node.item)
	# 				node.right = Node(item)
	# 			else:
	# 				self.__insert(item, node.right)

	def search(self, item=None):
		current = self.root
		if self.root == None: 
			return None
		while item != current.item:
			if item < current.item:
				current = current.left
			else:
				current = current.right
			if current == None: 
				return None
		return current

	def preorder_traversal(self, node=None):
		if node != None:
			print(node.item, end=' ')
			self.preorder_traversal(node.left)
			self.preorder_traversal(node.right)

	def inorder_traversal(self, node=None):
		if node != None:
			self.inorder_traversal(node.left)
			print(node.item, end=' ')
			self.inorder_traversal(node.right)

	def postorder_traversal(self, node=None):
		if node != None:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print(node.item, end=' ')


	def traversal(self, opt='preorder'):
		"""
		opt = 
		'prevorder': root, left right
		'inorder': left, root, right
		'postorder': left, right, root
		"""
		if opt == 'preorder':
			self.preorder_traversal(self.root)
			print()
		elif opt == 'inorder':
			self.inorder_traversal(self.root)
			print()
		elif opt == 'postorder':
			self.postorder_traversal(self.root)
			print()
		else:
			ValueError("Error: opt must be \'preorder\'/\'inorder\'/\'postorder\'.")
