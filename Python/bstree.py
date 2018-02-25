"""
implementation of Binary Search Tree
"""
"""
Not finished yet
"""

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

class BSTree:
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
		current = self.root:
		while current:
		if self.root == None:
			self.root = Node(item)
		else:
			current = self.root
			while True:
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

	def search(self, item=None):
		"""
		return Node if found Node.item == item
		return None otherwise
		"""
		if self.root == None: 
			return None
		current = self.root
		while item != current.item:
			if item < current.item:
				current = current.left
			else:
				current = current.right
			if current == None: 
				return None
		return current

	def isIn(self, item=None):
		current = self.root
		while current:
			if item < current.item:
				current = current.left
			elif item > current.item:
				current = current.right
			else: # current == current.item
				return True
		return False

	def delete(self, item=None):
		"""
		case1: deleted node has no child
				1. node == root 
				2. node != root
		case2: deleted node has one child
				1. node == root
				2. node != root
		case3: deleted node has two children
				1. node == root
				2. node != root
		"""
		# if node:
		# 	# case1
		# 	if not node.left and not node.right:
		# 		...
		# 	# case2
		# 	elif (is node.left) not (is node.right):
		# 		...
		# 	# case3
		# 	elif node.left and node.right:
		# 		...

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
